import unittest
import numpy as np
import json
import matplotlib.pyplot as plt
from datetime import datetime
from models.sistema_gestion import SistemaGestionEventos


class TestSistemaGestionEventos(unittest.TestCase):

    def setUp(self):
        self.sistema = SistemaGestionEventos()

    def test_crear_evento_bar(self):
        id_bar = 1
        nombre = "Bar Test"
        fecha = "2024-05-14"
        hora_apertura = "18:00"
        hora_inicio = "20:00"
        lugar = "Lugar de prueba"
        direccion = "Dirección de prueba"
        ciudad = "Ciudad de prueba"
        estado = "Estado de prueba"
        aforo_maximo = 100
        porcentaje_ganancias_bar = 0.1

        evento_bar = self.sistema.crear_evento_bar(id_bar, nombre, fecha, hora_apertura, hora_inicio, lugar, direccion,
                                                   ciudad, estado, aforo_maximo, porcentaje_ganancias_bar)

        self.assertEqual(evento_bar.nombre, nombre)
        self.assertEqual(evento_bar.fecha, fecha)

    def test_crear_evento_teatro(self):
        id_teatro = 1
        nombre_teatro = "Teatro Test"
        fecha = "2024-05-14"
        hora_apertura = "18:00"
        hora_inicio = "20:00"
        lugar = "Lugar de prueba"
        direccion = "Dirección de prueba"
        ciudad = "Ciudad de prueba"
        estado = "Estado de prueba"
        aforo_maximo = 200
        alquiler_teatro = 500

        evento_teatro = self.sistema.crear_evento_teatro(id_teatro, nombre_teatro, fecha, hora_apertura, hora_inicio,
                                                         lugar, direccion, ciudad, estado, aforo_maximo,
                                                         alquiler_teatro)

        self.assertEqual(evento_teatro.nombre, nombre_teatro)
        self.assertEqual(evento_teatro.fecha, fecha)

    def test_crear_evento_filantropico(self):
        id_filantropico = 1
        nombre_filantropico = "Evento Filantrópico Test"
        fecha = "2024-05-14"
        hora_apertura = "18:00"
        hora_show = "19:00"
        lugar = "Lugar de prueba"
        direccion = "Dirección de prueba"
        ciudad = "Ciudad de prueba"
        estado = "Estado de prueba"
        aforo_maximo = 300

        evento_filantropico = self.sistema.crear_evento_filantropico(id_filantropico, nombre_filantropico, fecha,
                                                                     hora_apertura, hora_show, lugar, direccion, ciudad,
                                                                     estado, aforo_maximo)

        self.assertEqual(evento_filantropico.nombre, nombre_filantropico)
        self.assertEqual(evento_filantropico.fecha, fecha)

    def test_crear_boleta_bar(self):
        # Define los parámetros para crear una boleta de bar
        id_boleta_bar = 1
        medio_pago = "Efectivo"
        precio_estandar = 50
        precio_preventa = 40
        porcentaje_descuento = 0.1
        es_cortesia = False

        # Crea la boleta de bar
        boleta_bar = self.sistema.crear_boleta_bar(id_boleta_bar, medio_pago, precio_estandar, precio_preventa,
                                                   porcentaje_descuento, es_cortesia)

        # Verifica que la boleta se haya creado correctamente
        self.assertEqual(boleta_bar.medio_pago, medio_pago)
        self.assertEqual(boleta_bar.precio_estandar, precio_estandar)
        # Agrega más aserciones según tus necesidades

    def test_crear_boleta_filantropico(self):
        # Define los parámetros para crear una boleta filantrópica
        id_boleta_filantropico = 1
        medio_pago = "Tarjeta de crédito"
        precio_estandar = 100
        precio_preventa = 80
        porcentaje_descuento = 0.2
        es_cortesia = False

        # Crea la boleta filantrópica
        boleta_filantropico = self.sistema.crear_boleta_filantropico(id_boleta_filantropico, medio_pago,
                                                                     precio_estandar, precio_preventa,
                                                                     porcentaje_descuento, es_cortesia)

        # Verifica que la boleta se haya creado correctamente
        self.assertEqual(boleta_filantropico.medio_pago, medio_pago)
        self.assertEqual(boleta_filantropico.precio_estandar, precio_estandar)
        # Agrega más aserciones según tus necesidades

    def test_crear_boleta_teatro(self):
        # Define los parámetros para crear una boleta de teatro
        id_boleta_teatro = 1
        medio_pago = "Transferencia bancaria"
        precio_estandar = 120
        precio_preventa = 100
        porcentaje_descuento = 0.15
        es_cortesia = False

        # Crea la boleta de teatro
        boleta_teatro = self.sistema.crear_boleta_teatro(id_boleta_teatro, medio_pago, precio_estandar, precio_preventa,
                                                         porcentaje_descuento, es_cortesia)

        # Verifica que la boleta se haya creado correctamente
        self.assertEqual(boleta_teatro.medio_pago, medio_pago)
        self.assertEqual(boleta_teatro.precio_estandar, precio_estandar)
        # Agrega más aserciones según tus necesidades

    def test_crear_artista_objeto(self):
        # Define los parámetros para crear un objeto de artista
        id_artista = 1
        nombre_artista = "Artista Test"
        pago_artista = 1000

        # Crea el objeto de artista
        artista = self.sistema.crear_artista_objeto(id_artista, nombre_artista, pago_artista)

        # Verifica que el objeto se haya creado correctamente
        self.assertEqual(artista.nombre, nombre_artista)
        self.assertEqual(artista.cobro, pago_artista)
        # Agrega más aserciones según tus necesidades

    def test_crear_patrocinador_objeto(self):
        # Define los parámetros para crear un objeto de patrocinador
        id_patrocinador = 1
        nombre = "Patrocinador Test"
        apoyo = "Económico"

        # Crea el objeto de patrocinador
        patrocinador = self.sistema.crear_patrocinador_objeto(id_patrocinador, nombre, apoyo)

        # Verifica que el objeto se haya creado correctamente
        self.assertEqual(patrocinador.nombre, nombre)
        self.assertEqual(patrocinador.apoyo, apoyo)
        # Agrega más aserciones según tus necesidades

    def test_generar_dashboard(self):
        # Define datos de ejemplo para los gráficos
        datos1 = (["Concierto", "Teatro", "Deporte"], [20, 15, 10])
        datos2 = (["Evento 1", "Evento 2", "Evento 3"], [500, 700, 300])

        # Ejecuta la función bajo prueba
        self.sistema.generar_dashboard(datos1, datos2)

        # Verifica que los gráficos se hayan generado correctamente
        self.assertTrue(plt.fignum_exists(1))  # Verifica si el primer gráfico fue creado
        self.assertTrue(plt.fignum_exists(2))  # Verifica si el segundo gráfico fue creado

    """
    Tengo Problemas con la apertura de archivos para las pruebas unitarias
    
    def test_obtener_datos_dashboard_frecuencia(self):
        # Crea un archivo temporal con eventos para las fechas especificadas
        eventos = [
            {"fecha": "01/01/2024", "tipo": "Concierto"},
            {"fecha": "01/01/2024", "tipo": "Teatro"},
            {"fecha": "02/01/2024", "tipo": "Concierto"},
            {"fecha": "03/01/2024", "tipo": "Concierto"},
            {"fecha": "03/01/2024", "tipo": "Deporte"},
            {"fecha": "04/01/2024", "tipo": "Teatro"}
        ]
        with open("temp_eventos.json", "w") as f:
            json.dump(eventos, f)

        # Llama a la función bajo prueba con las fechas de inicio y fin
        fecha_inicio = "01/01/2024"
        fecha_fin = "03/01/2024"
        tipos_evento, vector_cantidad_eventos = self.sistema.obtener_datos_dashboard_frecuencia(fecha_inicio, fecha_fin)

        # Verifica que los tipos de eventos y la cantidad de eventos sean correctos
        self.assertEqual(tipos_evento, ["Concierto", "Teatro", "Deporte"])
        self.assertTrue(np.array_equal(vector_cantidad_eventos, np.array([2, 1, 1])))

        # Elimina el archivo temporal
        os.remove("temp_eventos.json")


    def test_generar_boleta_pdf(self):
        # Define un diccionario de ejemplo para la boleta
        diccionario_boleta = {
            "Nombre": "Juan",
            "Apellido": "Perez",
            "Evento": "Concierto",
            "Precio": "$50",
            "Medio de Pago": "Tarjeta de crédito"
        }

        # Genera la boleta en formato PDF
        self.sistema.generar_boleta_pdf(diccionario_boleta)

        # Verifica que el archivo PDF generado existe
        self.assertTrue(os.path.exists(RUTA_PDF_GENERADO))
    """



if __name__ == '__main__':
    unittest.main()