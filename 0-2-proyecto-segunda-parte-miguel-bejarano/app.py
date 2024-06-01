# Punto de Arranque de la aplicacion
import streamlit as st

from controllers.gui_controller import GuiController

# Configuro el nombre de la pagina, icono, ancho del layout
st.set_page_config(page_title="Eventos de Comedia Toxicomicos", page_icon="🤣", layout = "wide",)

if __name__ == "__main__":
    gui = GuiController()
    gui.main()