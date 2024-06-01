import streamlit as st
from models.sistema_gestion import SistemaGestionEventos
from view.main_view import dibujar_pagina_inicial


class GuiController:
    def __init__(self):
        """
        Constructor de la clase GuiController.

        Inicializa el sistema de gestión de eventos si no está presente en la sesión de Streamlit.
        """
        if 'estado_app' not in st.session_state:
            self.sistema_gestion = SistemaGestionEventos()
            self.run_page = 'main'

    def main(self):
        """
        Función principal para la gestión de la interfaz de usuario.

        Llama a la función 'dibujar_pagina_inicial' para renderizar la página principal.
        """
        if self.run_page == 'main':
            dibujar_pagina_inicial(self)
