import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import plotly.graph_objects as go
import time
import base64

# --- IMPORTACIÓN DE DATOS ---
try:
    from catalogo import (
        CATALOGO_INDICADORES, 
        LISTA_AGRUPAMIENTOS, 
        LISTA_UNIDADES, 
        LISTA_DESAGREGACION, 
        LISTA_FUENTES, 
        MAPA_PAISES, 
        MAPA_DERECHOS
    )
except ImportError:
    st.error("❌ Error Crítico: No se encontró el archivo 'catalogo.py'.")
    st.stop()

# Función auxiliar para imágenes
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Protocolo de San Salvador - Eclíptica", page_icon="🌎", layout="wide")

# --- 2. TEXTOS ---
TEXTOS = {
    "ES": {
        "title": "Protocolo de San Salvador", 
        "nav_load": "Gestión de Registros",
        "nav_view": "Dashboard",
        "sidebar_config": "Configuración",
        "dark_mode": "Modo Oscuro",
        "meta_country": "País del Informe (*)",
        "meta_right": "Derecho Asignado (*)",
        "meta_year": "Año del Informe (*)",
        "val_header": "Registro de Indicadores",
        "manual_btn": "Agregar al Lote",
        "btn_save": "Guardar Lote en Base de Datos",
        "btn_discard": "Descartar Lote",
        "view_title": "Registros del Protocolo",
        "view_refresh": "Actualizar Tablero",
        "toast_save": "Datos guardados correctamente.",
        "dash_expander_table": "Detalle de Registros",
        "err_missing_meta": "⚠️ ¡ALTO! Debes seleccionar PAÍS, DERECHO y AÑO en la parte superior antes de continuar.",
        "chk_no_espec": "Marcar como 'No Específico'"
    },
    "EN": {
        "title": "San Salvador Protocol", 
        "nav_load": "Record Management",
        "nav_view": "Control Dashboard",
        "sidebar_config": "Configuration",
        "dark_mode": "Dark Mode",
        "meta_country": "Report Country (*)",
        "meta_right": "Assigned Right (*)",
        "meta_year": "Report Year (*)",
        "val_header": "Indicator Registration",
        "manual_btn": "Add to Batch",
        "btn_save": "Save Batch to Database",
        "btn_discard": "Discard Batch",
        "view_title": "Historical Database",
        "view_refresh": "Refresh Dashboard",
        "toast_save": "Data saved successfully.",
        "dash_expander_table": "Record Details",
        "err_missing_meta": "⚠️ STOP! You must select COUNTRY, RIGHT, and YEAR at the top before proceeding.",
        "chk_no_espec": "Mark as 'Non-Specific'"
    }
}

# --- 3. FUNCIONES ---
def generar_uid(row, pais_nombre, anio_informe, derecho_seleccionado):
    try:
        code_pais = "UNK"
        for nombre, codigo in MAPA_PAISES.items():
            if nombre in pais_nombre:
                code_pais = codigo; break
        cat_raw = str(row.get("CATEGORÍA", "X")).strip().upper()
        code_cat = cat_raw[0] if cat_raw else "X"
        code_anio = str(anio_informe)[-2:]
        code_ref = str(row.get("REF_INDICADOR", "000"))
        code_der = MAPA_DERECHOS.get(derecho_seleccionado, "OTR")
        return f"{code_pais}-{code_cat}-{code_anio}-{code_ref}-{code_der}"
    except: return "ERR"

@st.cache_resource
def conectar_google_sheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    if "gcp_service_account" in st.secrets:
        creds_dict = st.secrets["gcp_service_account"]
        credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    else:
        credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
        
    gc = gspread.authorize(credentials)
    sh = gc.open("Protocolo San Salvador")
    try: return sh.worksheet("Base_Datos")
    except: return sh.get_worksheet(0)

def guardar_en_sheet(df):
    ws = conectar_google_sheet()
    ws.append_rows(df.values.tolist())

def cargar_datos_sheet():
    ws = conectar_google_sheet()
    data = ws.get_all_records()
    return pd.DataFrame(data)

# --- FUNCIONES DASHBOARD ---
def calcular_metas_catalogo(derecho_filtro=None):
    meta_total = 0
    metas_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}
    
    for derecho, agrupamientos in CATALOGO_INDICADORES.items():
        if derecho_filtro and derecho not in derecho_filtro:
            continue
        for agrup, categorias in agrupamientos.items():
            for cat_nombre, lista_inds in categorias.items():
                cantidad = len(lista_inds)
                meta_total += cantidad
                cat_norm = cat_nombre.strip()
                if "Estructural" in cat_norm: metas_cat["Estructurales"] += cantidad
                elif "Proceso" in cat_norm: metas_cat["Procesos"] += cantidad
                elif "Resultado" in cat_norm: metas_cat["Resultados"] += cantidad
    
    return meta_total, metas_cat

def crear_donut(valor, meta, color_fill, color_empty, titulo_centro, text_color):
    fig = go.Figure(data=[go.Pie(
        labels=['Completado', 'Faltante'],
        values=[valor, max(0, meta - valor)],
        hole=.75,
        marker=dict(colors=[color_fill, color_empty]),
        textinfo='none',
        sort=False,
        hoverinfo='label+value'
    )])
    
    fig.update_layout(
        showlegend=False,
        annotations=[dict(
            text=titulo_centro, 
            x=0.5, y=0.5, 
            font_size=24, 
            showarrow=False, 
            font=dict(color=text_color, family="Arial", weight="bold")
        )],
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=280
    )
    return fig

# --- 4. INTERFAZ ---
st.markdown('<div class="sticky-header">', unsafe_allow_html=True)
header_container = st.container()

with header_container:
    col_title, col_nav, col_settings = st.columns([1.5, 2.5, 1])
    
    with col_settings:
        sub_c1, sub_c2 = st.columns([1.2, 0.8])
        with sub_c1:
            idioma = st.selectbox("", ["Español", "English"], index=0, label_visibility="collapsed", key="lang_sel_top")
            lang = "ES" if idioma == "Español" else "EN"
            T = TEXTOS[lang]
        with sub_c2:
            if "dark_mode" not in st.session_state: st.session_state.dark_mode = False
            icon_display = "🌙" if st.session_state.dark_mode else "☀️"
            if st.button(icon_display, key="btn_theme_toggle", use_container_width=True):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
            dark_mode = st.session_state.dark_mode

    with col_title:
         title_color = "#F2F2F2" if dark_mode else "#011936"
         st.markdown(f"<h3 style='margin:0; padding-top:15px; font-weight:700; color:{title_color};'>{T['title']}</h3>", unsafe_allow_html=True)

    with col_nav:
        modo_app = st.radio(
            "",
            [T['nav_load'], T['nav_view']],
            index=0, 
            horizontal=True,
            label_visibility="collapsed"
        )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---") 

img_base64 = get_base64_image("watermark_protocolo.png")

# --- CSS STYLING ---
if dark_mode:
    # --- MODO OSCURO ---
    st.markdown(f"""
    <style>
    .stApp {{ background-color: #011936; color: #F2F2F2; }}
    .stApp::before {{
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: 80%; background-position: center; background-repeat: no-repeat;
        background-attachment: fixed; opacity: 0.08; filter: grayscale(100%) invert(1); z-index: 0; pointer-events: none;
    }}
    .sticky-header {{
        position: fixed; top: 0; left: 0; width: 100%; z-index: 99999;
        background-color: rgba(0, 15, 31, 0.85); backdrop-filter: blur(12px);
        padding-bottom: 15px; padding-top: 10px; border-bottom: 1px solid rgba(70, 83, 98, 0.5);
    }}
    .main .block-container {{ z-index: 1; position: relative; padding-top: 8rem !important; }}
    .stApp > header {{ display: none !important; }}
    
    /* NAV */
    div[data-testid="stRadio"] label {{ 
        background-color: transparent !important; color: #B0B0B0 !important; 
        padding: 8px 20px; border-radius: 20px; font-weight: 600; border: 1px solid transparent; 
        transition: all 0.3s ease;
    }}
    div[data-testid="stRadio"] label:hover {{
        background-color: #465362 !important; color: #FFFFFF !important; border-color: #F2F2F2 !important;
        transform: scale(1.05); cursor: pointer;
    }}
    div[role="radiogroup"] label[data-checked="true"] {{ 
        background-color: #9D8420 !important; color: #FFFFFF !important; 
        border: 1px solid #9D8420 !important; box-shadow: 0px 4px 12px rgba(0,0,0,0.5) !important;
    }}
    div[data-testid="stRadio"] > div {{ display: flex; justify_content: center; gap: 20px; align-items: center; }}
    div[role="radiogroup"] > label > div:first-child {{ display: none !important; }}

    /* CONTENEDORES */
    div[data-testid="stMetric"], div[data-testid="stForm"], .stDataFrame {{ 
        background-color: #465362; border: 1px solid #9D8420; border-radius: 8px; padding: 15px; 
    }}
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetricLabel {{ color: #F2F2F2 !important; }}
    
    /* BOTONES GENERALES (SECUNDARIOS) */
    div.stButton > button {{ 
        background-color: #E0E0E0 !important; color: #011936 !important; 
        border: 1px solid #9D8420 !important; font-weight: bold !important; transition: all 0.3s ease; 
    }}
    div.stButton > button:hover {{ 
        background-color: #9D8420 !important; color: #F2F2F2 !important; border-color: #F2F2F2 !important; 
    }}

    /* BOTONES PRIMARY (AGREGAR AL LOTE / ACTUALIZAR TABLERO) */
    div.stButton > button[kind="primary"] {{
        background-color: #FFFFFF !important;
        color: #011936 !important;
        border: 2px solid #011936 !important;
    }}
    div.stButton > button[kind="primary"]:hover {{
        background-color: #FFF59D !important; /* AMARILLO CLARO */
        color: #011936 !important; 
        border-color: #011936 !important;
    }}
    
    /* EXPANDER (DETALLE REGISTROS) */
    div[data-testid="stExpander"] {{
        background-color: #011936 !important; /* Azul Oscuro */
        border: 1px solid #465362 !important; 
        color: #FFFFFF !important; /* Fuente Blanca */
    }}
    div[data-testid="stExpander"] details summary {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] details summary:hover {{ color: #9D8420 !important; }}
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] * {{ color: #FFFFFF !important; }}

    /* HOVER SELECTBOX (DARK) */
    .stSelectbox div[data-baseweb="select"] > div {{
        transition: border-color 0.3s ease !important;
    }}
    .stSelectbox div[data-baseweb="select"] > div:hover {{
        border-color: #F2F2F2 !important;
        cursor: pointer;
    }}

    section[data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)
else:
    # --- MODO CLARO ---
    st.markdown(f"""
    <style>
    .stApp {{ background-color: #F2F2F2; color: #011936; }}
    .stApp::before {{
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: 80%; background-position: center; background-repeat: no-repeat;
        background-attachment: fixed; opacity: 0.08; filter: grayscale(100%); z-index: 0; pointer-events: none;
    }}
    .sticky-header {{
        position: fixed; top: 0; left: 0; width: 100%; z-index: 99999;
        background-color: rgba(224, 224, 224, 0.85); backdrop-filter: blur(12px);
        padding-bottom: 15px; padding-top: 10px; border-bottom: 2px solid #9D8420;
    }}
    .main .block-container {{ z-index: 1; position: relative; padding-top: 8rem !important; }}
    .stApp > header {{ display: none !important; }}
    
    /* NAV */
    div[role="radiogroup"] > label > div:first-child {{ display: none !important; }}
    div[data-testid="stRadio"] label {{ 
        background-color: transparent; color: #465362 !important; font-weight: 400 !important;
        border-radius: 20px !important; padding: 8px 20px; border: 1px solid transparent; 
        transition: all 0.3s ease; margin-right: 10px;
    }}
    div[data-testid="stRadio"] label:hover {{
        background-color: #E0E0E0 !important; color: #011936 !important; cursor: pointer;
    }}
    div[role="radiogroup"] label[data-checked="true"] {{ 
        background-color: #011936 !important; color: #FFFFFF !important; 
        border: 2px solid #011936 !important; box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
    }}
    div[role="radiogroup"] label[data-checked="true"] p {{ color: #FFFFFF !important; }}
    
    /* INPUTS & DROPDOWNS */
    .stSelectbox div[data-baseweb="select"] > div, .stTextInput input {{
        background-color: #011936 !important; color: #FFFFFF !important; border: 1px solid #465362 !important;
    }}
    .stSelectbox div[data-baseweb="select"] div {{
        color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; font-weight: 400 !important;
    }}
    div[data-baseweb="select"] svg {{ fill: #FFFFFF !important; }}
    ul[data-baseweb="menu"] {{ background-color: #011936 !important; }}
    li[data-baseweb="option"] {{ color: #FFFFFF !important; }}
    
    /* HOVER SELECTBOX (LIGHT) */
    .stSelectbox div[data-baseweb="select"] > div {{
        transition: border-color 0.3s ease !important;
    }}
    .stSelectbox div[data-baseweb="select"] > div:hover {{
        border-color: #9D8420 !important;
        cursor: pointer;
    }}

    /* BOTONES GENERALES (SECUNDARIOS) */
    div.stButton > button {{ 
        background-color: #011936 !important; color: #FFFFFF !important; border: 2px solid #011936; 
        border-radius: 8px; font-weight: 500 !important;
    }}
    div.stButton > button:hover {{ 
        background-color: #9D8420 !important; color: #FFFFFF !important; border-color: #9D8420 !important;
    }}

    /* BOTONES PRIMARY (AGREGAR AL LOTE / ACTUALIZAR TABLERO) */
    div.stButton > button[kind="primary"] {{
        background-color: #FFFFFF !important;
        color: #011936 !important;
        border: 2px solid #011936 !important;
    }}
    div.stButton > button[kind="primary"]:hover {{
        background-color: #FFF59D !important; /* AMARILLO CLARO */
        color: #011936 !important; 
        border-color: #011936 !important;
    }}
    
    /* EXPANDER (DETALLE REGISTROS) */
    div[data-testid="stExpander"] {{ 
        background-color: #011936 !important; /* Azul Oscuro */
        border: 1px solid #011936; border-radius: 8px; 
        color: #FFFFFF !important; /* Fuente Blanca */
    }}
    div[data-testid="stExpander"] * {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] input {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] div[data-baseweb="select"] div {{ color: #FFFFFF !important; }}

    p, h1, h2, h3, h4, h5, h6, label, .stMarkdown, .stRadio label {{ color: #011936 !important; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

# --- MÓDULO 1: GESTIÓN MANUAL (YA SIN IA) ---
if modo_app == T["nav_load"]:
    
    # Header de Selección Global
    c_meta1, c_meta2, c_meta3 = st.columns(3)
    with c_meta1:
        pais_sel = st.selectbox(T["meta_country"], list(MAPA_PAISES.keys()), index=None, placeholder="Seleccione un país...")
    with c_meta2:
        der_sel = st.selectbox(T["meta_right"], list(MAPA_DERECHOS.keys()), index=None, placeholder="Seleccione un derecho...")
    with c_meta3:
        anio_sel = st.selectbox(T["meta_year"], range(2000, 2031), index=None, placeholder="Seleccione año...")
    
    st.markdown("---")
    
    # Formulario Manual (Ahora ocupa todo el ancho)
    st.subheader(T["val_header"])
    if "df_ia" not in st.session_state: st.session_state.df_ia = pd.DataFrame()
    
    # Contenedor del Formulario
    with st.container(border=True):
        if not der_sel:
            st.warning("⚠️ Selecciona un 'Derecho Asignado' arriba para cargar las listas correspondientes.")
        else:
            if der_sel in CATALOGO_INDICADORES:
                agrupamientos_disp = list(CATALOGO_INDICADORES[der_sel].keys())
            else:
                agrupamientos_disp = ["No hay datos cargados"]
            
            # Fila 1: Clasificación
            c_f1_1, c_f1_2 = st.columns(2)
            with c_f1_1:
                m_agr = st.selectbox("Agrupamiento", agrupamientos_disp, key="sel_agr")
            
            categorias_disp = []
            if der_sel in CATALOGO_INDICADORES and m_agr in CATALOGO_INDICADORES[der_sel]:
                categorias_disp = list(CATALOGO_INDICADORES[der_sel][m_agr].keys())
            
            with c_f1_2:
                m_cat = st.selectbox("Categoría", categorias_disp if categorias_disp else ["Estructural", "Proceso", "Resultado"], key="sel_cat")
            
            # Fila 2: Indicador
            indicadores_obj = []
            if der_sel in CATALOGO_INDICADORES and m_agr in CATALOGO_INDICADORES[der_sel] and m_cat in CATALOGO_INDICADORES[der_sel][m_agr]:
                indicadores_obj = CATALOGO_INDICADORES[der_sel][m_agr][m_cat]
            
            opciones_ind = [f"[{x[0]}] {x[1]}" for x in indicadores_obj]
            seleccion_ind = st.selectbox("Indicador", opciones_ind if opciones_ind else ["Otro / Personalizado"], key="sel_ind")
            
            if seleccion_ind and "[" in seleccion_ind:
                ref_auto = seleccion_ind.split("]")[0].replace("[", "")
                nombre_ind = seleccion_ind.split("] ")[1]
            else:
                ref_auto = "000"
                nombre_ind = seleccion_ind
            
            st.caption(f"📌 Referencia Técnica: **{ref_auto}**")

            # Fila 3: Detalles y Datos
            st.markdown("---")
            c1, c2 = st.columns(2)
            with c1:
                m_des = st.selectbox("Desagregación", LISTA_DESAGREGACION, key="sel_des")
                m_uni = st.selectbox("Unidad", LISTA_UNIDADES, key="sel_uni")
            
            # CAMBIO AQUÍ: Layout para Valor y Checkbox juntos
            with c2:
                col_valor_input, col_valor_chk = st.columns([0.65, 0.35]) # 65% Input, 35% Checkbox
                
                with col_valor_chk:
                    # Espaciadores para alinear verticalmente el checkbox con el input
                    st.write("") 
                    st.write("") 
                    is_no_especifico = st.checkbox(T["chk_no_espec"], key="chk_no_espec")

                with col_valor_input:
                    if is_no_especifico:
                        m_val = st.text_input("Valor", value="NO ESPECÍFICO", disabled=False, key="input_val_dis")
                    else:
                        m_val = st.text_input("Valor", key="input_val")
                
                m_fue = st.selectbox("Fuente", LISTA_FUENTES, key="sel_fue")
            
            # Botón Agregar (TIPO PRIMARY)
            if st.button(T["manual_btn"], type="primary", use_container_width=True):
                if not pais_sel or not der_sel or not anio_sel:
                    st.error(T["err_missing_meta"])
                else:
                    with st.spinner("Agregando..."):
                            no_esp_value = "TRUE" if is_no_especifico else "FALSE"
                            new_row = {
                                "DERECHO":der_sel, "CATEGORÍA":m_cat, "AGRUPAMIENTO":m_agr, 
                                "REF_INDICADOR":ref_auto, "INDICADOR":nombre_ind, 
                                "DESAGREGACIÓN":m_des, "UNIDAD":m_uni, "AÑO":anio_sel, 
                                "VALOR":m_val, "FUENTE":m_fue, "ESTADO_DATO":"Manual",
                                "NO_ESPECIFICO": no_esp_value
                            }
                            st.session_state.df_ia = pd.concat([st.session_state.df_ia, pd.DataFrame([new_row])], ignore_index=True)
                            time.sleep(0.2)
                            st.rerun()

    # Tabla de Previsualización (Lote actual)
    if not st.session_state.df_ia.empty:
        st.subheader("Lote en Preparación")
        df_work = st.session_state.df_ia.copy()
        df_work["UID"] = df_work.apply(lambda r: generar_uid(r, pais_sel, anio_sel, der_sel), axis=1)
        
        cols = ["UID", "DERECHO", "CATEGORÍA", "INDICADOR", "AGRUPAMIENTO", "DESAGREGACIÓN", "UNIDAD", "AÑO", "VALOR", "FUENTE", "ESTADO_DATO", "NO_ESPECIFICO", "REF_INDICADOR"]
        for c in cols: 
            if c not in df_work.columns: df_work[c]=""
        
        df_fin = st.data_editor(df_work[cols], num_rows="dynamic", height=300, use_container_width=True)
        
        cb1, cb2 = st.columns(2)
        with cb1:
            if st.button(T["btn_save"], type="secondary", use_container_width=True):
                try:
                    guardar_en_sheet(df_fin)
                    st.toast(T["toast_save"], icon="🎉")
                    st.balloons()
                    st.session_state.df_ia = pd.DataFrame()
                    st.rerun()
                except Exception as e: st.error(str(e))
        with cb2:
            if st.button(T["btn_discard"], use_container_width=True):
                st.session_state.df_ia = pd.DataFrame()
                st.rerun()
    else:
        st.info("El lote está vacío. Agrega registros manualmente arriba.")

# --- MÓDULO 2: VISUALIZACIÓN ---
elif modo_app == T["nav_view"]:
    st.subheader(T["view_title"])
    # CAMBIO AQUÍ: Botón Actualizar ahora es PRIMARY
    if st.button(T["view_refresh"], type="primary"):
        st.cache_data.clear()
        st.rerun()
    
    try:
        df_historico = cargar_datos_sheet()
        if not df_historico.empty:
            # --- FILTROS ---
            c_fil1, c_fil2, c_fil3 = st.columns(3)
            with c_fil1:
                filtro_pais = st.multiselect("Filtrar por País", df_historico["UID"].astype(str).str.split("-").str[0].unique())
            with c_fil2:
                filtro_derecho = st.multiselect("Filtrar por Derecho", df_historico["DERECHO"].unique())
            with c_fil3:
                df_historico["AÑO"] = df_historico["AÑO"].astype(str)
                filtro_anio = st.multiselect("Filtrar por Año", sorted(df_historico["AÑO"].unique()))
            
            # --- FILTRADO DATOS ---
            df_show = df_historico.copy()
            if filtro_pais:
                df_show = df_show[df_show["UID"].astype(str).str.split("-").str[0].isin(filtro_pais)]
            if filtro_derecho:
                df_show = df_show[df_show["DERECHO"].isin(filtro_derecho)]
            if filtro_anio:
                df_show = df_show[df_show["AÑO"].isin(filtro_anio)]
            
            # --- CÁLCULOS DE PROGRESO ---
            indicadores_cargados_total = df_show["REF_INDICADOR"].nunique() if not df_show.empty else 0
            
            cargados_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}
            if not df_show.empty and "CATEGORÍA" in df_show.columns:
                for cat in df_show["CATEGORÍA"].unique():
                    cat_str = str(cat).strip()
                    count = df_show[df_show["CATEGORÍA"] == cat]["REF_INDICADOR"].nunique()
                    if "Estructural" in cat_str: cargados_cat["Estructurales"] += count
                    elif "Proceso" in cat_str: cargados_cat["Procesos"] += count
                    elif "Resultado" in cat_str: cargados_cat["Resultados"] += count

            # Cálculo de METAS
            meta_total_calculada, metas_por_categoria = calcular_metas_catalogo(filtro_derecho if filtro_derecho else None)
            
            # --- VISUALIZACIÓN ---
            st.divider()
            
            text_color_charts = "#F2F2F2" if dark_mode else "#011936"
            color_missing = "#ff4444"
            
            # Gráfico Principal
            col_main_chart = st.columns([1, 2, 1])
            with col_main_chart[1]:
                st.markdown(f"<h3 style='text-align: center; color:{text_color_charts}'>Progreso Global</h3>", unsafe_allow_html=True)
                fig_main = crear_donut(
                    indicadores_cargados_total, 
                    meta_total_calculada, 
                    "#00C851", 
                    color_missing, 
                    f"{indicadores_cargados_total} / {meta_total_calculada}",
                    text_color_charts
                )
                st.plotly_chart(fig_main, use_container_width=True)

            # Gráficos Secundarios
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"<h5 style='text-align: center; color:{text_color_charts}'>Estructurales</h5>", unsafe_allow_html=True)
                fig_est = crear_donut(cargados_cat["Estructurales"], metas_por_categoria["Estructurales"], "#33b5e5", color_missing, f"{cargados_cat['Estructurales']}/{metas_por_categoria['Estructurales']}", text_color_charts)
                st.plotly_chart(fig_est, use_container_width=True)
            with c2:
                st.markdown(f"<h5 style='text-align: center; color:{text_color_charts}'>Procesos</h5>", unsafe_allow_html=True)
                fig_proc = crear_donut(cargados_cat["Procesos"], metas_por_categoria["Procesos"], "#ffbb33", color_missing, f"{cargados_cat['Procesos']}/{metas_por_categoria['Procesos']}", text_color_charts)
                st.plotly_chart(fig_proc, use_container_width=True)
            with c3:
                st.markdown(f"<h5 style='text-align: center; color:{text_color_charts}'>Resultados</h5>", unsafe_allow_html=True)
                fig_res = crear_donut(cargados_cat["Resultados"], metas_por_categoria["Resultados"], "#aa66cc", color_missing, f"{cargados_cat['Resultados']}/{metas_por_categoria['Resultados']}", text_color_charts)
                st.plotly_chart(fig_res, use_container_width=True)

            st.divider()
            with st.expander(T["dash_expander_table"]):
                st.dataframe(df_show, use_container_width=True, height=600)
        else:
            st.warning("La hoja de cálculo está vacía o no se pudo leer.")
            
    except Exception as e:
        st.error(f"Error al conectar con Google Sheets: {e}")
