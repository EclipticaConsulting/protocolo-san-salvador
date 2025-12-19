import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import google.generativeai as genai
import PyPDF2
import json
import plotly.express as px
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
        "meta_country": "País del Informe (*)",
        "meta_right": "Derecho Asignado (*)",
        "meta_year": "Año del Informe (*)",
        "val_header": "2. Validación y Carga",
        "manual_header": "Registro Manual de Datos",
        "manual_btn": "Agregar Registro",
        "btn_save": "Guardar en Base de Datos",
        "btn_discard": "Descartar Cambios",
        "view_title": "Centro de Monitoreo",
        "view_refresh": "Actualizar Tablero",
        "dash_chart_bar": "Análisis Comparativo",
        "dash_expander_table": "Detalle de Registros",
        "upload_header": "1. Conexión de Documentos",
        "upload_label": "Cargar Archivo PDF",
        "api_label": "Clave de API (Gemini)",
        "start_page": "Página Inicial",
        "end_page": "Página Final",
        "btn_extract": "Iniciar Extracción Automática",
        "processing": "Procesando página {current} de {total}...",
        "quota_switch": "Cuota excedida en {model}. Cambiando...",
        "toast_save": "Datos guardados correctamente.",
        "range_label": "Rango de Lectura"
    },
    "EN": {
        "title": "San Salvador Protocol", 
        "nav_load": "Record Management",
        "nav_view": "Control Dashboard",
        "meta_country": "Report Country (*)",
        "meta_right": "Assigned Right (*)",
        "meta_year": "Report Year (*)",
        "val_header": "2. Validation & Upload",
        "manual_header": "Manual Data Entry",
        "manual_btn": "Add Record",
        "btn_save": "Save to Database",
        "btn_discard": "Discard Changes",
        "view_title": "Monitoring Center",
        "view_refresh": "Refresh Dashboard",
        "dash_chart_bar": "Comparative Analysis",
        "dash_expander_table": "Record Details",
        "upload_header": "1. Document Connection",
        "upload_label": "Upload PDF File",
        "api_label": "API Key (Gemini)",
        "start_page": "Start Page",
        "end_page": "End Page",
        "btn_extract": "Start Auto-Extraction",
        "processing": "Processing page {current} of {total}...",
        "quota_switch": "Quota exceeded on {model}. Switching...",
        "toast_save": "Data saved successfully.",
        "range_label": "Reading Range"
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
        try:
            credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)
        except: return None
    gc = gspread.authorize(credentials)
    sh = gc.open("Protocolo San Salvador")
    try: return sh.worksheet("Base_Datos")
    except: return sh.get_worksheet(0)

def guardar_en_sheet(df):
    ws = conectar_google_sheet()
    if ws: ws.append_rows(df.values.tolist())

def cargar_datos_sheet():
    ws = conectar_google_sheet()
    if ws:
        data = ws.get_all_records()
        return pd.DataFrame(data)
    return pd.DataFrame()

def procesar_pagina_individual(texto, api_key, anio, T):
    genai.configure(api_key=api_key)
    modelos = ['models/gemini-2.0-flash-lite', 'models/gemini-flash-latest', 'models/gemini-2.0-flash']
    prompt = f"""
    Actúa como experto en el Protocolo de San Salvador. Extrae TODOS los indicadores.
    CONTEXTO: Año informe: {anio}.
    INSTRUCCIONES:
    1. REF_INDICADOR: "0" (siempre).
    2. AGRUPAMIENTO: Intenta clasificar en: Recepción, Contexto, Capacidades, Igualdad, Info, Justicia.
    TEXTO: {texto}
    SALIDA JSON: [{{ "CATEGORÍA": "Estructural|Proceso|Resultado", "AGRUPAMIENTO": "Categoría", "REF_INDICADOR": "0", "INDICADOR": "Texto del indicador", "DESAGREGACIÓN": "...", "UNIDAD": "...", "AÑO": "{anio}", "VALOR": "...", "FUENTE": "...", "ESTADO_DATO": "Oficial" }}]
    """
    for m in modelos:
        try:
            time.sleep(1)
            model = genai.GenerativeModel(m)
            res = model.generate_content(prompt)
            data = json.loads(res.text.replace("```json","").replace("```","").strip())
            return pd.DataFrame(data), "OK"
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e):
                st.toast(T["quota_switch"].format(model=m), icon="⚠️")
                continue
    return pd.DataFrame(), "ERROR"

def calcular_metas_catalogo(derecho_filtro=None):
    meta_total = 0
    metas_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}
    for derecho, agrupamientos in CATALOGO_INDICADORES.items():
        # V47: Ajuste para "Todos" (Title Case)
        if derecho_filtro and derecho_filtro != "Todos":
            if derecho != derecho_filtro: continue
            
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
    restante = max(0, meta - valor)
    fig = go.Figure(data=[go.Pie(
        labels=['Completado', 'Faltante'],
        values=[valor, restante],
        hole=.75,
        marker=dict(colors=[color_fill, color_empty]),
        textinfo='none',
        sort=False,
        hoverinfo='label+value'
    )])
    fig.update_layout(
        showlegend=False,
        annotations=[dict(text=titulo_centro, x=0.5, y=0.5, font_size=24, showarrow=False, font=dict(color=text_color, family="Arial", weight="bold"))],
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=280
    )
    return fig

# --- INTERFAZ ---
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
        if "nav_index" not in st.session_state: st.session_state.nav_index = 0
        opciones_nav = [T['nav_load'], T['nav_view']]
        if st.session_state.nav_index >= len(opciones_nav): st.session_state.nav_index = 0
        modo_app = st.radio("", opciones_nav, index=st.session_state.nav_index, horizontal=True, label_visibility="collapsed", key="nav_radio")
        if modo_app == T['nav_load']: st.session_state.nav_index = 0
        else: st.session_state.nav_index = 1

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---") 

img_base64 = get_base64_image("watermark_protocolo.png")

if dark_mode:
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
    div[data-testid="stMetric"], div[data-testid="stForm"], .stDataFrame {{ 
        background-color: #465362; border: 1px solid #9D8420; border-radius: 8px; padding: 15px; 
    }}
    div[data-testid="metric-container"] {{ display: flex; justify-content: center; flex-direction: column; align-items: center; }}
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetricLabel {{ color: #F2F2F2 !important; }}
    div[data-testid="stMetricValue"] {{ color: #9D8420 !important; }}
    div.stButton > button {{ 
        background-color: #E0E0E0 !important; color: #011936 !important; 
        border: 1px solid #9D8420 !important; font-weight: bold !important; transition: all 0.3s ease; 
    }}
    div.stButton > button p {{ color: #011936 !important; }}
    div.stButton > button:hover {{ 
        background-color: #9D8420 !important; border-color: #F2F2F2 !important; 
    }}
    div.stButton > button:hover p {{ color: #F2F2F2 !important; }}
    div[data-testid="stExpander"] {{
        background-color: #465362 !important; border: 0px solid rgba(255,255,255,0.1) !important; color: #F2F2F2 !important;
    }}
    div[data-testid="stExpander"] details summary {{ color: #F2F2F2 !important; }}
    div[data-testid="stExpander"] details summary:hover {{ color: #9D8420 !important; }}
    div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] p {{ color: #F2F2F2 !important; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)
else:
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
    .stSelectbox div[data-baseweb="select"] > div, .stTextInput input {{
        background-color: #011936 !important; color: #FFFFFF !important; border: 1px solid #465362 !important;
    }}
    .stSelectbox div[data-baseweb="select"] div {{
        color: #FFFFFF !important; -webkit-text-fill-color: #FFFFFF !important; font-weight: 400 !important;
    }}
    div[data-baseweb="select"] svg {{ fill: #FFFFFF !important; }}
    ul[data-baseweb="menu"] {{ background-color: #011936 !important; }}
    li[data-baseweb="option"] {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] {{ 
        background-color: #011936 !important; border: 1px solid #011936; border-radius: 8px; color: #FFFFFF !important; 
    }}
    div[data-testid="stExpander"] * {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] input {{ color: #FFFFFF !important; }}
    div[data-testid="stExpander"] div[data-baseweb="select"] div {{ color: #FFFFFF !important; }}
    .stButton button, [data-testid="stFileUploader"] button {{ 
        background-color: #011936 !important; color: #FFFFFF !important; border: 2px solid #011936; 
        border-radius: 8px; font-weight: 500 !important;
    }}
    .stButton button:hover {{ 
        background-color: #9D8420 !important; color: #FFFFFF !important; border-color: #9D8420 !important;
    }}
    .stButton button p {{ color: inherit !important; }}
    p, h1, h2, h3, h4, h5, h6, label, .stMarkdown, .stRadio label {{ color: #011936 !important; }}
    div[data-testid="stMetricLabel"] {{ color: #011936 !important; }}
    div[data-testid="stMetricValue"] {{ color: #9D8420 !important; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

# --- MÓDULO 1: CARGA DE DATOS ---
if modo_app == T["nav_load"]:
    c_meta1, c_meta2, c_meta3 = st.columns(3)
    with c_meta1:
        pais_sel = st.selectbox(T["meta_country"], list(MAPA_PAISES.keys()), index=None, placeholder="Seleccione un país...")
    with c_meta2:
        der_sel = st.selectbox(T["meta_right"], list(MAPA_DERECHOS.keys()), index=None, placeholder="Seleccione un derecho...")
    with c_meta3:
        anio_sel = st.selectbox(T["meta_year"], range(2000, 2031), index=None, placeholder="Seleccione año...")
    
    st.markdown("---")
    
    col_izq, col_der = st.columns([1, 1.5], gap="large")
    with col_izq:
        st.subheader(T["upload_header"])
        uploaded_file = st.file_uploader(T["upload_label"], type="pdf")
        api_key = st.text_input(T["api_label"], type="password")
        if uploaded_file and api_key:
            reader = PyPDF2.PdfReader(uploaded_file)
            num_pages = len(reader.pages)
            st.info(f"📄 {num_pages} págs.")
            c1, c2 = st.columns(2)
            with c1: start = st.number_input(T["start_page"], 1, num_pages, 1)
            with c2: end = st.number_input(T["end_page"], start, num_pages, min(start+4, num_pages))
            if st.button(T["btn_extract"], type="primary"):
                if not pais_sel or not der_sel or not anio_sel:
                    st.error(T["err_missing_meta"])
                else:
                    df_acum = pd.DataFrame()
                    prog = st.progress(0)
                    status = st.empty()
                    for i in range(start-1, end):
                        try: txt = reader.pages[i].extract_text()
                        except: txt = ""
                        status.text(T["processing"].format(current=i+1, total=end))
                        df_pag, st_code = procesar_pagina_individual(txt, api_key, anio_sel, T)
                        if st_code == "OK" and not df_pag.empty:
                            df_pag["DERECHO"] = der_sel
                            df_acum = pd.concat([df_acum, df_pag], ignore_index=True)
                        prog.progress((i - start + 2)/(end - start + 1))
                    prog.empty(); status.empty()
                    if not df_acum.empty:
                        base_count = 1
                        if "df_ia" in st.session_state and not st.session_state.df_ia.empty:
                            base_count = len(st.session_state.df_ia) + 1
                        df_acum["REF_INDICADOR"] = [f"{x:03d}" for x in range(base_count, base_count+len(df_acum))]
                        if "df_ia" not in st.session_state: st.session_state.df_ia = pd.DataFrame()
                        st.session_state.df_ia = pd.concat([st.session_state.df_ia, df_acum], ignore_index=True)

    with col_der:
        st.subheader(T["val_header"])
        if "df_ia" not in st.session_state: st.session_state.df_ia = pd.DataFrame()
        with st.expander(T["manual_header"], expanded=True):
            if not der_sel:
                st.warning("⚠️ Selecciona un 'Derecho Asignado' arriba para ver las listas.")
            else:
                if der_sel in CATALOGO_INDICADORES:
                    agrupamientos_disp = list(CATALOGO_INDICADORES[der_sel].keys())
                else:
                    agrupamientos_disp = ["No hay datos cargados"]
                m_agr = st.selectbox("Agrupamiento", agrupamientos_disp, key="sel_agr")
                categorias_disp = []
                if der_sel in CATALOGO_INDICADORES and m_agr in CATALOGO_INDICADORES[der_sel]:
                    categorias_disp = list(CATALOGO_INDICADORES[der_sel][m_agr].keys())
                m_cat = st.selectbox("Categoría", categorias_disp if categorias_disp else ["Estructural", "Proceso", "Resultado"], key="sel_cat")
                indicadores_obj = []
                if der_sel in CATALOGO_INDICADORES and m_agr in CATALOGO_INDICADORES[der_sel] and m_cat in CATALOGO_INDICADORES[der_sel][m_agr]:
                    indicadores_obj = CATALOGO_INDICADORES[der_sel][m_agr][m_cat]
                opciones_ind = [f"[{x[0]}] {x[1]}" for x in indicadores_obj]
                seleccion_ind = st.selectbox("Indicador", opciones_ind if opciones_ind else ["Otro / Personalizado"], key="sel_ind")
                if seleccion_ind and "[" in seleccion_ind:
                    ref_auto = seleccion_ind.split("]")[0].replace("[", "")
                    nombre_ind = seleccion_ind.split("] ")[1]
                else:
                    ref_auto = "000"; nombre_ind = seleccion_ind
                st.info(f"📌 Referencia Asignada: **{ref_auto}**")
                st.markdown("---")
                c1, c2 = st.columns(2)
                with c1:
                    m_des = st.selectbox("Desagregación", LISTA_DESAGREGACION, key="sel_des")
                    m_uni = st.selectbox("Unidad", LISTA_UNIDADES, key="sel_uni")
                with c2:
                    m_val = st.text_input("Valor", key="input_val")
                    m_fue = st.selectbox("Fuente", LISTA_FUENTES, key="sel_fue")
                if st.button(T["manual_btn"], type="primary", use_container_width=True):
                    if not pais_sel or not der_sel or not anio_sel:
                        st.error(T["err_missing_meta"])
                    else:
                        with st.spinner("Guardando..."):
                             new_row = {"DERECHO":der_sel, "CATEGORÍA":m_cat, "AGRUPAMIENTO":m_agr, "REF_INDICADOR":ref_auto, "INDICADOR":nombre_ind, "DESAGREGACIÓN":m_des, "UNIDAD":m_uni, "AÑO":anio_sel, "VALOR":m_val, "FUENTE":m_fue, "ESTADO_DATO":"Manual"}
                             st.session_state.df_ia = pd.concat([st.session_state.df_ia, pd.DataFrame([new_row])], ignore_index=True)
                             time.sleep(0.5)
                             st.rerun()

        if not st.session_state.df_ia.empty:
            df_work = st.session_state.df_ia.copy()
            df_work["UID"] = df_work.apply(lambda r: generar_uid(r, pais_sel, anio_sel, der_sel), axis=1)
            cols = ["UID", "DERECHO", "CATEGORÍA", "INDICADOR", "VALOR", "AÑO", "AGRUPAMIENTO", "REF_INDICADOR"]
            for c in cols: 
                if c not in df_work.columns: df_work[c]=""
            df_fin = st.data_editor(df_work[cols], num_rows="dynamic", height=400, use_container_width=True)
            cb1, cb2 = st.columns(2)
            with cb1:
                if st.button(T["btn_save"], type="secondary", use_container_width=True):
                    try:
                        guardar_en_sheet(df_fin)
                        st.toast(T["toast_save"], icon="🎉"); st.balloons(); st.session_state.df_ia = pd.DataFrame(); st.rerun()
                    except Exception as e: st.error(str(e))
            with cb2:
                if st.button(T["btn_discard"], use_container_width=True):
                    st.session_state.df_ia = pd.DataFrame(); st.rerun()

# --- MÓDULO 2: VISUALIZACIÓN ---
elif modo_app == T["nav_view"]:
    st.subheader(T["view_title"])
    if st.button(T["view_refresh"]):
        st.cache_data.clear(); st.rerun()
    
    try:
        df_historico = cargar_datos_sheet()
        
        c_fil1, c_fil2, c_fil3 = st.columns(3)
        list_paises = sorted(list(MAPA_PAISES.keys()))
        list_derechos = sorted(list(MAPA_DERECHOS.keys()))
        max_anio = 2024 
        if not df_historico.empty and "AÑO" in df_historico.columns:
            try: max_anio = int(df_historico["AÑO"].max())
            except: pass
        
        with c_fil1:
            # V47: Sin "TODOS", selección única
            filtro_pais = st.selectbox("Filtrar por País", list_paises, index=0)
        
        with c_fil2:
            # V47: "Todos" (Title Case)
            opciones_derecho = ["Todos"] + list_derechos
            filtro_derecho = st.selectbox("Filtrar por Derecho", opciones_derecho, index=0)
            
        with c_fil3:
            # V47: Sin "TODOS", selección única con default a max_anio si posible
            opciones_anio = [str(x) for x in range(2000, 2031)]
            try:
                idx_anio = opciones_anio.index(str(max_anio))
            except:
                idx_anio = 0
            filtro_anio = st.selectbox("Filtrar por Año (Dashboard)", opciones_anio, index=idx_anio)
        
        # --- LÓGICA DE FILTRADO ---
        if not df_historico.empty:
            df_show = df_historico.copy()
            # 1. País (Siempre filtra porque ya no hay TODOS)
            if filtro_pais in MAPA_PAISES:
                code_pais = MAPA_PAISES[filtro_pais]
                df_show = df_show[df_show["UID"].astype(str).str.startswith(code_pais)]
            
            # 2. Derecho (Filtra si != Todos)
            if filtro_derecho != "Todos":
                df_show = df_show[df_show["DERECHO"] == filtro_derecho]
                
            # 3. Año (Siempre filtra porque ya no hay TODOS)
            df_show = df_show[df_show["AÑO"].astype(str) == filtro_anio]
        else:
            df_show = pd.DataFrame()

        indicadores_cargados = df_show["REF_INDICADOR"].nunique() if not df_show.empty else 0
        cargados_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}
        if not df_show.empty and "CATEGORÍA" in df_show.columns:
            for cat in df_show["CATEGORÍA"].unique():
                cat_str = str(cat).strip()
                count = df_show[df_show["CATEGORÍA"] == cat]["REF_INDICADOR"].nunique()
                if "Estructural" in cat_str: cargados_cat["Estructurales"] += count
                elif "Proceso" in cat_str: cargados_cat["Procesos"] += count
                elif "Resultado" in cat_str: cargados_cat["Resultados"] += count

        meta_total, metas_cat = calcular_metas_catalogo(filtro_derecho if filtro_derecho else None)
        
        st.divider()
        text_color = "#F2F2F2" if dark_mode else "#011936"
        color_missing = "#ff4444"
        
        col_main = st.columns([1, 2, 1])
        with col_main[1]:
            st.markdown(f"<h3 style='text-align:center; color:{text_color}'>Progreso Global</h3>", unsafe_allow_html=True)
            st.plotly_chart(crear_donut(indicadores_cargados, meta_total, "#00C851", color_missing, f"{indicadores_cargados}/{meta_total}", text_color), use_container_width=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'>Estructurales</h5>", unsafe_allow_html=True)
            st.plotly_chart(crear_donut(cargados_cat["Estructurales"], metas_cat["Estructurales"], "#33b5e5", color_missing, f"{cargados_cat['Estructurales']}/{metas_cat['Estructurales']}", text_color), use_container_width=True)
        with c2:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'>Procesos</h5>", unsafe_allow_html=True)
            st.plotly_chart(crear_donut(cargados_cat["Procesos"], metas_cat["Procesos"], "#ffbb33", color_missing, f"{cargados_cat['Procesos']}/{metas_cat['Procesos']}", text_color), use_container_width=True)
        with c3:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'>Resultados</h5>", unsafe_allow_html=True)
            st.plotly_chart(crear_donut(cargados_cat["Resultados"], metas_cat["Resultados"], "#aa66cc", color_missing, f"{cargados_cat['Resultados']}/{metas_cat['Resultados']}", text_color), use_container_width=True)

        st.divider()

        st.markdown(f"<h3 style='color:{text_color}'>{T['dash_chart_bar']}</h3>", unsafe_allow_html=True)
        
        if not df_show.empty:
            indicadores_disponibles = sorted(df_show["INDICADOR"].unique())
        else:
            indicadores_disponibles = []
            
        c_ana1, c_ana2 = st.columns([2, 1])
        with c_ana1:
            sel_ind_comp = st.selectbox("Seleccione Indicador para Comparar", indicadores_disponibles)
        with c_ana2:
            anios_disp_ind = []
            if sel_ind_comp and not df_show.empty:
                anios_disp_ind = sorted(df_show[df_show["INDICADOR"] == sel_ind_comp]["AÑO"].unique().astype(str))
            # V47: Este se mantiene como MULTISELECT para poder comparar años
            sel_anios_comp = st.multiselect("Seleccione Años", anios_disp_ind, default=anios_disp_ind)

        if sel_ind_comp and sel_anios_comp and not df_show.empty:
            df_chart = df_show[(df_show["INDICADOR"] == sel_ind_comp) & (df_show["AÑO"].astype(str).isin(sel_anios_comp))].copy()
            df_chart.sort_values("AÑO", ascending=True, inplace=True)
            fig_bar = px.bar(
                df_chart,
                y="AÑO", x="VALOR", orientation='h',
                text="VALOR", color="AÑO", title=f"Evolución: {sel_ind_comp}"
            )
            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color=text_color), showlegend=False,
                xaxis_title="Valor Registrado", yaxis_title="Año del Informe",
                yaxis=dict(type='category')
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Seleccione un indicador y años para ver la comparativa.")

        st.divider()
        with st.expander(T["dash_expander_table"]):
            st.dataframe(df_show, use_container_width=True, height=600)
            
    except Exception as e:
        st.error(f"Error en el Dashboard: {e}")
