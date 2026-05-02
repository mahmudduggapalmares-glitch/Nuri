import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Configuración de la página
st.set_page_config(page_title="Para mi pequeña Nur", page_icon="✨", layout="centered")

def load_lottieurl(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Intentar cargar las animaciones (si fallan, el código no se romperá)
lottie_celebration = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_u4yrau.json")
lottie_support = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_sSF63S.json")

st.markdown("""
    <style>
    .big-font { font-size:50px !important; color: #ff4b4b; text-align: center; font-weight: bold; }
    .sub-font { font-size:25px !important; text-align: center; color: #31333F; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">¡Feliz Cumpleaños, Nur! 🎂</p>', unsafe_allow_html=True)

# Solo muestra la animación si se cargó correctamente
if lottie_celebration:
    st_lottie(lottie_celebration, height=300, key="coding")

st.markdown('<p class="sub-font">Siempre serás mi pequeña Nur, hoy y siempre.</p>', unsafe_allow_html=True)

st.write("---")

col1, col2 = st.columns(2)

with col1:
    # Cambiado "Promesa" por algo más suave
    st.subheader("🌟 Desde el corazón")
    st.write("""
    Quiero que sepas que siempre estaré aquí para ti. No importa cuánto crezcas, 
    siempre contarás con mi apoyo para lo que necesites, ya sea una ayuda 
    grande o solo alguien que te escuche.
    """)

with col2:
    if lottie_support:
        st_lottie(lottie_support, height=150, key="support")

st.write("---")
st.subheader("📩 ¿Necesitas algo?")
st.info("Cualquier cosa que necesites, por pequeña que sea, cuenta conmigo.")

with st.expander("Haz clic aquí si necesitas ayuda con algo o quieres decirme algo"):
    ayuda = st.text_area("Escribe aquí lo que necesites:")
    if st.button("Enviar"):
        st.success("¡Mensaje enviado! Estaré ahí para ti. ❤️")

st.markdown("---")
st.write("Con todo mi cariño, siempre a tu lado.")
