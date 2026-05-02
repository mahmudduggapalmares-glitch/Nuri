import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Configuración de la página
st.set_page_config(page_title="Feliz Cumpleaños Nur", page_icon="✨", layout="centered")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Recursos visuales
lottie_celebration = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_u4yrau.json")
lottie_support = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_sSF63S.json")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .big-font {
        font-size:50px !important;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
    }
    .sub-font {
        font-size:25px !important;
        text-align: center;
        color: #31333F;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown('<p class="big-font">¡Feliz Cumpleaños, Nur! 🎂</p>', unsafe_allow_html=True)
st_lottie(lottie_celebration, height=300, key="coding")

# Mensaje Principal
st.markdown('<p class="sub-font">Siempre serás la pequeña Nur frente a mí.</p>', unsafe_allow_html=True)

st.write("---")

# Secciones de compromiso y apoyo
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌟 Mi Promesa")
    st.write("""
    Quiero que sepas que, sin importar cuánto pase el tiempo, 
    siempre estaré aquí para ser tu apoyo incondicional. 
    Mi mano siempre estará extendida para ti.
    """)

with col2:
    st_lottie(lottie_support, height=150, key="support")

st.write("---")

# Sección interactiva de ayuda
st.subheader("📩 ¿Necesitas algo?")
st.info("No importa si es algo pequeño o un gran desafío, cuenta conmigo.")

with st.expander("Haz clic aquí si necesitas ayuda con algo ahora mismo"):
    ayuda = st.text_area("Escribe aquí lo que necesites o simplemente un mensaje para mí:")
    if st.button("Enviar mensaje"):
        st.success("¡Mensaje recibido! Estaré ahí para ti en un abrir y cerrar de ojos. ❤️")

# Pie de página
st.markdown("---")
st.write("Con todo mi cariño y apoyo siempre.")

