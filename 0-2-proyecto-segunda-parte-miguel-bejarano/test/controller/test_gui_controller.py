import unittest
from unittest.mock import patch, MagicMock
from controllers.gui_controller import GuiController

"""
patch: Esta función es un decorador/context manager que se utiliza para simular (mock) comportamientos durante las
 pruebas. Permite reemplazar partes de tu sistema que quieres probar con objetos mock. Esto es útil cuando tienes partes
  de tu sistema que son difíciles de probar, como llamadas a bases de datos o a servicios externos.  
  
MagicMock: Es una subclase de Mock con métodos mágicos predefinidos (aquellos métodos que empiezan y terminan con doble
 guión bajo, como __getitem__, __setitem__, etc.) y que soporta la mayoría de los métodos que puedes llamar en un
  objeto. Esto es útil cuando necesitas simular un objeto que tiene métodos mágicos.
"""

class TestGuiController(unittest.TestCase):

    @patch('streamlit.session_state', MagicMock())
    @patch('controllers.gui_controller.dibujar_pagina_inicial')
    def test_main(self, mock_dibujar_pagina_inicial):
        # Arrange
        gui_controller = GuiController()

        # Act
        gui_controller.main()

        # Assert
        mock_dibujar_pagina_inicial.assert_called_once_with(gui_controller)


if __name__ == '__main__':
    unittest.main()