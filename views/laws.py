import streamlit as st

# Pasa el estado de la sesion
authenticator = st.session_state['authenticator']

st.title("Leyes")
try:
    authenticator.login("unrendered")
except Exception as e:
    st.error(e)