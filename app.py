# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import plotly.graph_objects as go
import time
import base64
import re
import unicodedata

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

# -----------------------------
# Helpers UI/Assets
# -----------------------------
def get_base64_image(image_path: str) -> str:
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Protocolo de San Salvador - Eclíptica", page_icon="🌎", layout="wide")

# -----------------------------
# Texts
# -----------------------------
TEXTOS = {
    "ES": {
        "title": "Protocolo de San Salvador",
        "nav_load": "Gestión de Registros",
        "nav_view": "Dashboard",
        "meta_country": "País del Informe (*)",
        "meta_right": "Derecho Asignado (*)",
        "meta_year": "Año del Informe (*)",
        "manual_header": "Registro Manual de Datos",
        "manual_btn": "Agregar a la Tabla",
        "btn_save": "Guardar en Base de Datos",
        "btn_discard": "Limpiar Tabla",
        "view_title": "Centro de Monitoreo",
        "view_refresh": "Actualizar Tablero",
        "dash_chart_bar": "Análisis Comparativo",
        "dash_expander_table": "Detalle de Registros",
        "toast_save": "Datos guardados correctamente."
    },
    "EN": {
        "title": "San Salvador Protocol",
        "nav_load": "Record Management",
        "nav_view": "Control Dashboard",
        "meta_country": "Report Country (*)",
        "meta_right": "Assigned Right (*)",
        "meta_year": "Report Year (*)",
        "manual_header": "Manual Data Entry",
        "manual_btn": "Add to Table",
        "btn_save": "Save to Database",
        "btn_discard": "Clear Table",
        "view_title": "Monitoring Center",
        "view_refresh": "Refresh Dashboard",
        "dash_chart_bar": "Comparative Analysis",
        "dash_expander_table": "Record Details",
        "toast_save": "Data saved successfully."
    }
}

# -----------------------------
# Data normalization (columns)
# -----------------------------
def _strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))

def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    df = df.copy()
    cols = []
    for c in df.columns:
        c2 = str(c).strip().upper()
        c2 = _strip_accents(c2)          # AÑO -> ANIO, CATEGORÍA -> CATEGORIA
        c2 = c2.replace(" ", "_")
        cols.append(c2)
    df.columns = cols

    alias = {
        "REFERENCIA_ASIGNADA": "REF_INDICADOR",
        "REF": "REF_INDICADOR",
        "CATEGORIA": "CATEGORIA",
        "ANO": "ANIO",
        "AÑO": "ANIO"
    }
    df.rename(columns=alias, inplace=True)
    return df

def asegurar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_columnas(df)
    cols_req = [
        "UID", "DERECHO", "AGRUPAMIENTO", "CATEGORIA", "INDICADOR", "REF_INDICADOR",
        "DESAGREGACION", "VALOR", "UNIDAD", "ANIO", "PAIS", "FUENTE", "ESTADO_DATO", "NOTA"
    ]
    for c in cols_req:
        if c not in df.columns:
            df[c] = ""
    return df[cols_req]

# -----------------------------
# UID (robust)
# -----------------------------
def generar_uid(row, pais_nombre, anio_informe, derecho_seleccionado):
    try:
        if not pais_nombre:
            return "ERR-PAIS"
        code_pais = MAPA_PAISES.get(pais_nombre, "UNK")

        cat_raw = str(row.get("CATEGORÍA", row.get("CATEGORIA", row.get("CATEGORIA", "X")))).strip().upper()
        cat_raw = _strip_accents(cat_raw)
        code_cat = cat_raw[0] if cat_raw and cat_raw != "NONE" else "X"

        code_anio = str(anio_informe)[-2:] if anio_informe else "00"
        code_ref = str(row.get("REF_INDICADOR", "000")).strip() or "000"
        code_der = MAPA_DERECHOS.get(derecho_seleccionado, "OTR")
        return f"{code_pais}-{code_cat}-{code_anio}-{code_ref}-{code_der}"
    except Exception:
        return "ERR"

# -----------------------------
# Google Sheets connection
# -----------------------------
@st.cache_resource
def conectar_google_sheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = st.secrets["gcp_service_account"]
            credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        else:
            # Fallback dev ONLY: credentials.json (avoid committing it)
            credentials = Credentials.from_service_account_file("credentials.json", scopes=scopes)

        gc = gspread.authorize(credentials)
        sh = gc.open("Protocolo San Salvador")
        try:
            return sh.worksheet("Base_Datos")
        except Exception:
            return sh.get_worksheet(0)
    except Exception:
        return None

def guardar_en_sheet(df: pd.DataFrame):
    ws = conectar_google_sheet()
    if not ws:
        raise RuntimeError("No se pudo conectar a Google Sheets. Revisa credenciales/st.secrets.")

    # Standardize columns (no tildes)
    df = asegurar_columnas(df)

    # Final cols (A-N)
    cols_finales = [
        "UID", "DERECHO", "AGRUPAMIENTO", "CATEGORIA", "INDICADOR", "REF_INDICADOR",
        "DESAGREGACION", "VALOR", "UNIDAD", "ANIO", "PAIS", "FUENTE", "ESTADO_DATO", "NOTA"
    ]
    df_ordenado = df.reindex(columns=cols_finales).fillna("")
    ws.append_rows(df_ordenado.values.tolist())

def cargar_datos_sheet():
    ws = conectar_google_sheet()
    if not ws:
        return pd.DataFrame()

    data = ws.get_all_records()
    df = pd.DataFrame(data)
    df = asegurar_columnas(df)
    return df

@st.cache_data(ttl=300)
def cargar_datos_sheet_cached():
    return cargar_datos_sheet()

# -----------------------------
# Save dedup (avoid duplicates)
# -----------------------------
def dedup_para_guardar(df: pd.DataFrame) -> pd.DataFrame:
    df = asegurar_columnas(df)
    key_cols = ["UID", "DESAGREGACION", "ANIO", "PAIS"]
    for c in key_cols:
        df[c] = df[c].astype(str).str.strip()
    df = df.drop_duplicates(subset=key_cols, keep="last")
    return df

# -----------------------------
# Catalog metas
# -----------------------------
def calcular_metas_catalogo(derecho_filtro=None):
    meta_total = 0
    metas_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}

    for derecho, agrupamientos in CATALOGO_INDICADORES.items():
        if derecho_filtro and derecho_filtro != "Todos" and derecho != derecho_filtro:
            continue

        for _, categorias in agrupamientos.items():
            for cat_nombre, lista_inds in categorias.items():
                cantidad = len(lista_inds)
                meta_total += cantidad

                cat_norm = cat_nombre.strip()
                if "Estructural" in cat_norm:
                    metas_cat["Estructurales"] += cantidad
                elif "Proceso" in cat_norm:
                    metas_cat["Procesos"] += cantidad
                elif "Resultado" in cat_norm:
                    metas_cat["Resultados"] += cantidad

    return meta_total, metas_cat

# -----------------------------
# Plotly donut
# -----------------------------
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
        annotations=[dict(
            text=f"<b>{titulo_centro}</b>",
            x=0.5, y=0.5,
            font_size=22,
            showarrow=False,
            font=dict(color=text_color, family="Arial Black")
        )],
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=280
    )
    return fig

# -----------------------------
# Value normalization (safe for % vs absolute)
# -----------------------------
def normalizar_valor(valor_str):
    """
    Retorna: (valor_numerico, texto, es_valido, es_porcentaje)
    """
    v = str(valor_str).strip()
    v_l = v.lower()

    # Binary
    if v_l in ["si", "sí", "yes", "cumple", "true"]:
        return 100.0, "SÍ", True, True
    if v_l in ["no", "no cumple", "false"]:
        return 0.0, "NO", True, True

    # Empty/other
    if not v_l or v_l in ["otro", "nan", "none", "incompleto", "."]:
        return 0.0, "Sin Dato", False, False

    # Detect percentage explicitly
    is_pct = "%" in v_l

    try:
        v_num = re.sub(r"[^\d.,-]", "", v_l)
        v_num = v_num.replace(",", ".")
        f = float(v_num)

        # heuristic
        es_porcentaje = is_pct or (0 <= f <= 100)
        return f, v, True, es_porcentaje
    except Exception:
        return 0.0, v, False, False

def clamp_0_100(x: float) -> float:
    try:
        return max(0.0, min(100.0, float(x)))
    except Exception:
        return 0.0

def preparar_serie_por_anio(df_context: pd.DataFrame, display_text: str, anios: list[str]) -> pd.DataFrame:
    if df_context.empty:
        return pd.DataFrame()

    d = df_context.copy()
    d = d[d["DISPLAY_TEXT"] == display_text]
    d = d[d["ANIO"].astype(str).isin([str(a) for a in anios])].copy()
    if d.empty:
        return pd.DataFrame()

    norm = d["VALOR"].apply(normalizar_valor)
    d["VAL_NUM"] = [x[0] for x in norm]
    d["VAL_TXT"] = [x[1] for x in norm]
    d["ES_VALIDO"] = [x[2] for x in norm]
    d["ES_PCT"] = [x[3] for x in norm]

    # Keep one row per year (prefer valid)
    d["__valid_rank"] = d["ES_VALIDO"].astype(int)
    d.sort_values(["ANIO", "__valid_rank"], ascending=[True, False], inplace=True)
    d = d.drop_duplicates(subset=["ANIO"], keep="first").copy()
    d.drop(columns=["__valid_rank"], inplace=True)

    d.sort_values("ANIO", inplace=True)
    return d

# -----------------------------
# UI Header + Theme
# -----------------------------
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
            if "dark_mode" not in st.session_state:
                st.session_state.dark_mode = False
            icon_display = "🌙" if st.session_state.dark_mode else "☀️"
            if st.button(icon_display, key="btn_theme_toggle", use_container_width=True):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
            dark_mode = st.session_state.dark_mode

    with col_title:
        title_color = "#F2F2F2" if dark_mode else "#011936"
        st.markdown(
            f"<h3 style='margin:0; padding-top:15px; font-weight:700; color:{title_color};'>{T['title']}</h3>",
            unsafe_allow_html=True
        )

    with col_nav:
        if "nav_index" not in st.session_state:
            st.session_state.nav_index = 0
        opciones_nav = [T['nav_load'], T['nav_view']]
        if st.session_state.nav_index >= len(opciones_nav):
            st.session_state.nav_index = 0
        modo_app = st.radio(
            "",
            opciones_nav,
            index=st.session_state.nav_index,
            horizontal=True,
            label_visibility="collapsed",
            key="nav_radio"
        )
        st.session_state.nav_index = 0 if modo_app == T['nav_load'] else 1

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

img_base64 = get_base64_image("watermark_protocolo.png")

# -----------------------------
# Theme CSS
# -----------------------------
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
    .stButton button {{
        background-color: #011936 !important; color: #FFFFFF !important; border: 2px solid #011936;
        border-radius: 8px; font-weight: 500 !important;
    }}
    .stButton button:hover {{
        background-color: #9D8420 !important; color: #FFFFFF !important; border-color: #9D8420 !important;
    }}
    .stButton button p {{ color: inherit !important; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# MODULE 1: DATA ENTRY
# =============================================================================
if modo_app == T["nav_load"]:
    c_meta1, c_meta2, c_meta3 = st.columns(3)
    with c_meta1:
        pais_sel = st.selectbox(T["meta_country"], list(MAPA_PAISES.keys()), index=None, placeholder="Seleccione un país...")
    with c_meta2:
        der_sel = st.selectbox(T["meta_right"], list(MAPA_DERECHOS.keys()), index=None, placeholder="Seleccione un derecho...")
    with c_meta3:
        anio_sel = st.selectbox(T["meta_year"], range(2000, 2031), index=None, placeholder="Seleccione año...")

    st.markdown("---")

    if "df_buffer" not in st.session_state:
        st.session_state.df_buffer = pd.DataFrame()

    with st.expander(T["manual_header"], expanded=True):
        if not der_sel:
            st.warning("⚠️ Selecciona un 'Derecho Asignado' arriba para ver las listas.")
        else:
            agrupamientos_disp = list(CATALOGO_INDICADORES.get(der_sel, {}).keys()) or ["No hay datos cargados"]
            m_agr = st.selectbox("Agrupamiento", agrupamientos_disp, key="sel_agr", index=None, placeholder="Seleccione agrupamiento...")

            categorias_disp = []
            if der_sel in CATALOGO_INDICADORES and m_agr and m_agr in CATALOGO_INDICADORES[der_sel]:
                categorias_disp = list(CATALOGO_INDICADORES[der_sel][m_agr].keys())

            m_cat = st.selectbox(
                "Categoría",
                categorias_disp if categorias_disp else ["Estructural", "Proceso", "Resultado"],
                key="sel_cat",
                index=None,
                placeholder="Seleccione categoría..."
            )

            indicadores_obj = []
            if der_sel in CATALOGO_INDICADORES and m_agr and m_cat and m_agr in CATALOGO_INDICADORES[der_sel] and m_cat in CATALOGO_INDICADORES[der_sel][m_agr]:
                indicadores_obj = CATALOGO_INDICADORES[der_sel][m_agr][m_cat]

            opciones_ind = [f"[{x[0]}] {x[1]}" for x in indicadores_obj]
            seleccion_ind = st.selectbox("Indicador", opciones_ind if opciones_ind else ["Otro / Personalizado"], key="sel_ind", index=None, placeholder="Seleccione indicador...")

            if seleccion_ind and "[" in seleccion_ind:
                ref_auto = seleccion_ind.split("]")[0].replace("[", "").strip()
                nombre_ind = seleccion_ind.split("] ")[1].strip()
            else:
                ref_auto = "000"
                nombre_ind = seleccion_ind if seleccion_ind else ""

            st.info(f"📌 Referencia Asignada: **{ref_auto}**")
            st.markdown("---")

            c1, c2 = st.columns([1, 1.5])

            with c1:
                m_des = st.selectbox("Desagregación", LISTA_DESAGREGACION, key="sel_des", index=None, placeholder="Seleccione...")
                m_uni = st.selectbox("Unidad", LISTA_UNIDADES, key="sel_uni", index=None, placeholder="Seleccione...")

            with c2:
                sc1, sc2, sc3 = st.columns([1.2, 1.5, 1.3])
                with sc1:
                    m_val = st.text_input("Valor", key="input_val")
                with sc2:
                    # Use neutral label color (works in both themes)
                    st.markdown("<label style='font-size:12px;'>Atributos</label>", unsafe_allow_html=True)
                    chk_progreso = st.checkbox("Señal de Progreso", key="chk_prog")
                    chk_transversal = st.checkbox("Principio Transversal", key="chk_tran")
                with sc3:
                    opciones_calidad = ["", "NO INFO", "INFO AMBIGUA", "NO APLICA"]
                    m_calidad = st.selectbox("Estado / Nota", opciones_calidad, key="sel_calidad")

                m_fue = st.selectbox("Fuente", LISTA_FUENTES, key="sel_fue", index=None, placeholder="Seleccione...")

            if st.button(T["manual_btn"], type="primary", use_container_width=True):
                if not pais_sel or not der_sel or not anio_sel or not seleccion_ind or not m_uni or not m_fue:
                    st.error("⚠️ Faltan campos obligatorios (País, Derecho, Año, Indicador, Unidad o Fuente).")
                else:
                    with st.spinner("Agregando..."):
                        partes_nota = []
                        if m_calidad:
                            partes_nota.append(m_calidad)

                        atributos = []
                        if chk_progreso:
                            atributos.append("Señal de Progreso")
                        if chk_transversal:
                            atributos.append("Principio Transversal")

                        if atributos:
                            partes_nota.append(", ".join(atributos))

                        nota_final = " | ".join(partes_nota) if partes_nota else ""

                        new_row = {
                            "DERECHO": der_sel,
                            "AGRUPAMIENTO": m_agr if m_agr else "",
                            "CATEGORIA": m_cat if m_cat else "",
                            "INDICADOR": nombre_ind,
                            "REF_INDICADOR": ref_auto,
                            "DESAGREGACION": m_des if m_des else "",
                            "VALOR": m_val,
                            "UNIDAD": m_uni,
                            "ANIO": anio_sel,
                            "PAIS": pais_sel,
                            "FUENTE": m_fue,
                            "ESTADO_DATO": "Manual",
                            "NOTA": nota_final
                        }

                        st.session_state.df_buffer = pd.concat(
                            [st.session_state.df_buffer, pd.DataFrame([new_row])],
                            ignore_index=True
                        )
                        time.sleep(0.05)
                        st.rerun()

    if not st.session_state.df_buffer.empty:
        df_work = asegurar_columnas(st.session_state.df_buffer.copy())

        # Build UID
        df_work["UID"] = df_work.apply(lambda r: generar_uid(r, pais_sel, anio_sel, der_sel), axis=1)

        cols_view = [
            "UID", "DERECHO", "AGRUPAMIENTO", "CATEGORIA", "INDICADOR",
            "REF_INDICADOR", "DESAGREGACION", "VALOR", "NOTA", "UNIDAD", "ANIO",
            "PAIS", "FUENTE", "ESTADO_DATO"
        ]

        st.divider()
        st.markdown("### Tabla de Datos (Pre-Carga)")

        df_fin = st.data_editor(df_work[cols_view], num_rows="dynamic", height=400, use_container_width=True)

        cb1, cb2 = st.columns(2)
        with cb1:
            if st.button(T["btn_save"], type="secondary", use_container_width=True):
                try:
                    df_to_save = dedup_para_guardar(df_fin)
                    guardar_en_sheet(df_to_save)
                    st.toast(T["toast_save"], icon="🎉")
                    st.balloons()
                    st.session_state.df_buffer = pd.DataFrame()
                    # only clear cached data reads
                    st.cache_data.clear()
                    st.rerun()
                except Exception as e:
                    st.error(str(e))
        with cb2:
            if st.button(T["btn_discard"], use_container_width=True):
                st.session_state.df_buffer = pd.DataFrame()
                st.rerun()

# =============================================================================
# MODULE 2: DASHBOARD
# =============================================================================
elif modo_app == T["nav_view"]:
    st.subheader(T["view_title"])
    if st.button(T["view_refresh"]):
        st.cache_data.clear()
        st.rerun()

    try:
        df_historico = cargar_datos_sheet_cached()
        df_historico = asegurar_columnas(df_historico)

        c_fil1, c_fil2, c_fil3 = st.columns(3)
        list_paises = sorted(list(MAPA_PAISES.keys()))
        list_derechos = sorted(list(MAPA_DERECHOS.keys()))

        max_anio = 2024
        if not df_historico.empty:
            try:
                max_anio = int(pd.to_numeric(df_historico["ANIO"], errors="coerce").max())
                if pd.isna(max_anio):
                    max_anio = 2024
            except Exception:
                max_anio = 2024

        with c_fil1:
            filtro_pais = st.selectbox("Filtrar por País", list_paises, index=0)
        with c_fil2:
            opciones_derecho = ["Todos"] + list_derechos
            filtro_derecho = st.selectbox("Filtrar por Derecho", opciones_derecho, index=0)
        with c_fil3:
            opciones_anio = [str(x) for x in range(2000, 2031)]
            idx_anio = opciones_anio.index(str(max_anio)) if str(max_anio) in opciones_anio else 0
            filtro_anio = st.selectbox("Filtrar por Año (Dashboard)", opciones_anio, index=idx_anio)

        if not df_historico.empty:
            df_base = df_historico.copy()

            # Country filter (robust)
            df_base = df_base[df_base["PAIS"].astype(str).str.strip() == str(filtro_pais).strip()]

            # Right filter
            if filtro_derecho != "Todos":
                df_base = df_base[df_base["DERECHO"] == filtro_derecho]

            # Optional: exclude rows marked explicitly as incompleto (kept for compatibility)
            # NOTE: your NOTA format is now different, so we only exclude exact match "INCOMPLETO"
            if "NOTA" in df_base.columns:
                df_base = df_base[df_base["NOTA"].astype(str).str.strip().str.upper() != "INCOMPLETO"]

            # DISPLAY TEXT
            df_base["DISPLAY_TEXT"] = df_base.apply(
                lambda x: f"[{str(x['REF_INDICADOR']).strip()}] {str(x['INDICADOR']).strip()}",
                axis=1
            )

            df_show_context = df_base.copy()
            df_show_kpi = df_base[df_base["ANIO"].astype(str) == str(filtro_anio)]
        else:
            df_show_kpi = pd.DataFrame()
            df_show_context = pd.DataFrame()

        # KPIs
        indicadores_cargados = df_show_kpi["REF_INDICADOR"].nunique() if not df_show_kpi.empty else 0
        cargados_cat = {"Estructurales": 0, "Procesos": 0, "Resultados": 0}

        if not df_show_kpi.empty:
            for cat in df_show_kpi["CATEGORIA"].unique():
                cat_str = str(cat).strip()
                count = df_show_kpi[df_show_kpi["CATEGORIA"] == cat]["REF_INDICADOR"].nunique()
                if "Estructural" in cat_str:
                    cargados_cat["Estructurales"] += count
                elif "Proceso" in cat_str:
                    cargados_cat["Procesos"] += count
                elif "Resultado" in cat_str:
                    cargados_cat["Resultados"] += count

        meta_total, metas_cat = calcular_metas_catalogo(filtro_derecho if filtro_derecho else None)

        st.divider()
        text_color = "#F2F2F2" if dark_mode else "#011936"
        color_missing = "#ff4444"

        col_main = st.columns([1, 2, 1])
        with col_main[1]:
            st.markdown(
                f"<h3 style='text-align:center; color:{text_color}'><b>Progreso Global ({filtro_anio})</b></h3>",
                unsafe_allow_html=True
            )
            st.plotly_chart(
                crear_donut(indicadores_cargados, meta_total, "#00C851", color_missing, f"{indicadores_cargados}/{meta_total}", text_color),
                use_container_width=True
            )

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'><b>Estructurales</b></h5>", unsafe_allow_html=True)
            st.plotly_chart(
                crear_donut(cargados_cat["Estructurales"], metas_cat["Estructurales"], "#33b5e5", color_missing,
                            f"{cargados_cat['Estructurales']}/{metas_cat['Estructurales']}", text_color),
                use_container_width=True
            )
        with c2:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'><b>Procesos</b></h5>", unsafe_allow_html=True)
            st.plotly_chart(
                crear_donut(cargados_cat["Procesos"], metas_cat["Procesos"], "#ffbb33", color_missing,
                            f"{cargados_cat['Procesos']}/{metas_cat['Procesos']}", text_color),
                use_container_width=True
            )
        with c3:
            st.markdown(f"<h5 style='text-align:center; color:{text_color}'><b>Resultados</b></h5>", unsafe_allow_html=True)
            st.plotly_chart(
                crear_donut(cargados_cat["Resultados"], metas_cat["Resultados"], "#aa66cc", color_missing,
                            f"{cargados_cat['Resultados']}/{metas_cat['Resultados']}", text_color),
                use_container_width=True
            )

        st.divider()
        st.markdown(f"<h3 style='color:{text_color}'><b>{T['dash_chart_bar']}</b></h3>", unsafe_allow_html=True)

        indicadores_disponibles = sorted(df_show_context["DISPLAY_TEXT"].unique()) if not df_show_context.empty else []

        c_ana1, c_ana2 = st.columns([2, 1])
        with c_ana1:
            sel_ind_comp = st.selectbox("Seleccione Indicador para Comparar", indicadores_disponibles)
        with c_ana2:
            full_years_list = [str(x) for x in range(2000, 2031)]
            anios_con_datos = []
            if sel_ind_comp and not df_show_context.empty:
                anios_con_datos = sorted(df_show_context[df_show_context["DISPLAY_TEXT"] == sel_ind_comp]["ANIO"].unique().astype(str))
            sel_anios_comp = st.multiselect("Seleccione Años", full_years_list, default=anios_con_datos)

        if sel_ind_comp and sel_anios_comp:
            df_chart = preparar_serie_por_anio(df_show_context, sel_ind_comp, sel_anios_comp)

            if df_chart.empty:
                st.warning(f"⚠️ No hay datos para '{sel_ind_comp}' en los años seleccionados.")
            elif not df_chart["ES_VALIDO"].any():
                st.warning(f"⚠️ El indicador '{sel_ind_comp}' no tiene datos válidos en los años seleccionados.")
            else:
                st.markdown(
                    f"<h4 style='text-align:center; color:{text_color}; margin-bottom:20px;'><b>{sel_ind_comp}</b></h4>",
                    unsafe_allow_html=True
                )

                cols = st.columns(len(df_chart))

                for i, (_, row) in enumerate(df_chart.iterrows()):
                    anio = str(row["ANIO"])
                    val_num = float(row["VAL_NUM"])
                    val_txt = row["VAL_TXT"]
                    es_pct = bool(row["ES_PCT"])

                    texto_mostrar = str(val_txt)
                    try:
                        if (not es_pct) and val_num >= 1000:
                            texto_mostrar = "{:,.0f}".format(val_num).replace(",", ".")
                    except Exception:
                        pass

                    if es_pct:
                        v100 = clamp_0_100(val_num)
                        if v100 >= 100:
                            color_anillo = "#27AE60"
                        elif v100 >= 50:
                            color_anillo = "#F2C94C"
                        else:
                            color_anillo = "#EB5757"
                        logrado = v100
                        restante = 100 - v100
                        label_a = "Logrado"
                        label_b = "Restante"
                    else:
                        color_anillo = "#33b5e5"
                        logrado = 100
                        restante = 0
                        label_a = "Valor"
                        label_b = ""

                    with cols[i]:
                        st.markdown(
                            f"<p style='text-align:center; font-weight:bold; font-size:18px; color:{text_color}; margin:0;'>{anio}</p>",
                            unsafe_allow_html=True
                        )

                        fig_donut = go.Figure(data=[go.Pie(
                            labels=[label_a, label_b] if label_b else [label_a, ""],
                            values=[logrado, restante],
                            hole=.75,
                            marker=dict(colors=[color_anillo, "rgba(128,128,128,0.2)"]),
                            textinfo='none',
                            sort=False,
                            hoverinfo='label+value'
                        )])

                        fig_donut.update_layout(
                            showlegend=False,
                            annotations=[dict(
                                text=f"<b>{texto_mostrar}</b>",
                                x=0.5, y=0.5,
                                font_size=24,
                                showarrow=False,    
                                font=dict(color=text_color, family="Arial Black")
                            )],
                            margin=dict(t=10, b=10, l=10, r=10),
                            height=220,
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)'
                        )

                        st.plotly_chart(fig_donut, use_container_width=True)

        elif not sel_ind_comp:
            st.info("👈 Seleccione un indicador arriba para comenzar el análisis.")
        else:
            st.info("Seleccione al menos un año para visualizar.")

        st.divider()
        with st.expander(T["dash_expander_table"]):
            st.dataframe(df_show_context, use_container_width=True, height=600)
    except Exception as e:
        st.error(f"❌ Error en el Dashboard: {e}")
