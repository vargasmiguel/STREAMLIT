import streamlit as st

st.title('📷 Cámara 📷')
pic=st.camera_input('Usa la :red[cámara] para tomar una :green[foto] $\sum$')

if pic:
    st.image(pic)

st.markdown("By Miguel y P$\\alpha$sc$\\alpha$l")

