import streamlit as st
from streamlit_option_menu import option_menu
# importamos las paginas
import views.account as account, views.home as home, views.laws as laws, views.strategy as strategy, views.writing as writing

st.set_page_config(
    page_title = "Opciones",
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": function
        })

    # Configuracion del menu. Los iconos son de bootstrap-icons
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title = 'Opciones',
                options = ['Inicio', 'Escritos', 'Estrategia', 'Leyes', 'Cuenta'],
                icons = ['house-fill', 'file-earmark-check-fill', 'pen-fill', 'archive-fill', 'gear-fill'],
                menu_icon = '',
                default_index = 1,
                styles = {
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-aling": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Laws":
            laws.app()
        if app == "Strategy":
            strategy.app()
        if app == "Writing":
            writing.app()

    run()