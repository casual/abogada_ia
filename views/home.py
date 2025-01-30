import streamlit as st

# Pasa el estado de la sesion
authenticator = st.session_state['authenticator']

def setup_home():
    st.title(f"Hola *{st.session_state['username']}* 👋")
    st.subheader("¿Qué necesitas hacer?")
    
    st.markdown("#")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Mejorar escritos", icon = ":material/task:", type = "primary"):
            st.switch_page("views/writing.py")
    with col2:
        if st.button("Crer estrategia", icon = ":material/psychology_alt:", type = "primary"):
            st.switch_page("views/strategy.py")
    with col3:
        if st.button("Buscar leyes",  icon = ":material/menu_book:", type = "primary"):
            st.switch_page("views/laws.py")




try:
    authenticator.login("unrendered")
    setup_home()
except Exception as e:
    st.error(e)