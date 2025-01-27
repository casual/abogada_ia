import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Configuraciones de paginas

home_page = st.Page(
    page = "views/home.py",
    title = "Inicio",
    icon = ":material/home:",
    default = True,
)

writing_page = st.Page(
    page = "views/writing.py",
    title = "Escritos",
    icon = ":material/task:",
)

strategy_page = st.Page(
    page = "views/strategy.py",
    title = "Estrategia",
    icon = ":material/psychology_alt:",
)

laws_page = st.Page(
    page = "views/laws.py",
    title = "Leyes",
    icon = ":material/menu_book:",
)

account_page = st.Page(
    page = "views/account.py",
    title = "Cuenta",
    icon = ":material/settings:",
)



def main():
    # Autenticador
    with open(".streamlit/config_auth.yaml") as file:
        config_auth = yaml.load(file, Loader = SafeLoader)
    # Para hashear las contraseñas
    #stauth.Hasher.hash_passwords(config['credentials'])

    authenticator = stauth.Authenticate(
        config_auth['credentials'],
        config_auth['cookie']['name'],
        config_auth['cookie']['key'],
        config_auth['cookie']['expiry_days']
    )

    st.session_state['authenticator'] = authenticator

    try:
        #authenticator.login(location = "main", fields = {'Form name':'Inicia sesión', 'Username':'Usuario', 'Password':'Contraseña', 'Login':'Iniciar sesión'})
        authenticator.login()
    except Exception as e:
        st.write(e)

    if st.session_state['authentication_status']:
        st.session_state['authenticator'] = authenticator
        st.logo("assets/logo.png")
        st.sidebar.text("Creado por 🧠")
        #st.sidebar.title(f"Sesion de *{st.session_state['username']}* 👋")
        authenticator.logout("Cerrar sesión", "sidebar")
        # Configuracion del menu
        pg = st.navigation(
            {
                "": [home_page], 
                "Herramientas":  [writing_page, strategy_page, laws_page],
                "Configuraciones": [account_page]
            }
        )
        pg.run()
    elif st.session_state['authentication_status'] is False:
        st.error("'Usuario o contraseña incorrectos'")
    elif st.session_state['authentication_status'] is None:
        st.warning("'Ingresa tu nombre de usuario y contraseña'")


if __name__ == "__main__":
    main()