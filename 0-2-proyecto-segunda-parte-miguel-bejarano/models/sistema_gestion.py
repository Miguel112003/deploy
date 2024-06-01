import streamlit as st
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from models.artista import Artista
from models.boleta import Boleta
from models.boleta_bar import BoletaBar
from models.boleta_filantropico import BoletaFilantropico
from models.boleta_teatro import BoletaTeatro
from models.evento import Evento
from models.filantropico import Filantropico
from models.patrocinador import Patrocinador
from models.bar import Bar
from models.teatro import Teatro
from settings import (RUTA_EVENTOS, RUTA_BOLETAS, RUTA_ARTISTAS, RUTA_PATROCINADORES, RUTA_CONTADORES, FECHA_ACTUAL,
                      RUTA_LOGO, RUTA_PDF_GENERADO, RUTA_QR)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from datetime import datetime


class SistemaGestionEventos:
    def __init__(self):
        """
        Inicializa el sistema de gestión de eventos.

        - Carga los eventos, boletas, artistas y patrocinadores desde los archivos JSON correspondientes.
        - Si los archivos no existen o están vacíos, inicializa las listas vacías.
        - Carga los contadores de IDs desde el archivo de contadores.
        - Si el archivo de contadores no existe o está vacío, inicializa los contadores en 1.

        Returns:
        - None
        """
        if os.path.exists(RUTA_EVENTOS) and os.path.getsize(RUTA_EVENTOS) > 0:
            with open(RUTA_EVENTOS, 'r') as f_eventos:
                self.eventos = json.load(f_eventos)
        else:
            self.eventos = []

        if os.path.exists(RUTA_BOLETAS) and os.path.getsize(RUTA_BOLETAS) > 0:
            with open(RUTA_BOLETAS, 'r') as f_boletas:
                self.boletas = json.load(f_boletas)
        else:
            self.boletas = []

        if os.path.exists(RUTA_ARTISTAS) and os.path.getsize(RUTA_ARTISTAS) > 0:
            with open(RUTA_ARTISTAS, 'r') as f_artistas:
                self.artistas = json.load(f_artistas)
        else:
            self.artistas = []

        if os.path.exists(RUTA_PATROCINADORES) and os.path.getsize(RUTA_PATROCINADORES) > 0:
            with open(RUTA_PATROCINADORES, 'r') as f_patrocinadores:
                self.patrocinadores = json.load(f_patrocinadores)
        else:
            self.patrocinadores = []

        if os.path.exists(RUTA_CONTADORES) and os.path.getsize(RUTA_CONTADORES) > 0:
            with open(RUTA_CONTADORES, 'r') as f_contadores:
                contadores = json.load(f_contadores)
                self.contador_id_eventos = contadores.get("contador_id_eventos", 1)
                self.contador_id_artistas = contadores.get("contador_id_artistas", 1)
                self.contador_id_boletas = contadores.get("contador_id_boletas", 1)
                self.contador_id_patrocinadores = contadores.get("contador_id_patrocinadores", 1)
        else:
            self.contador_id_eventos = 1
            self.contador_id_artistas = 1
            self.contador_id_boletas = 1
            self.contador_id_patrocinadores = 1

    def guardar_contadores(self):
        """
        Guarda los contadores actuales en un archivo JSON.

        Guarda los siguientes contadores:
        - contador_id_eventos: Contador de IDs de eventos.
        - contador_id_artistas: Contador de IDs de artistas.
        - contador_id_boletas: Contador de IDs de boletas.
        - contador_id_patrocinadores: Contador de IDs de patrocinadores.

        Returns:
        - None
        """
        contadores = {
            "contador_id_eventos": self.contador_id_eventos,
            "contador_id_artistas": self.contador_id_artistas,
            "contador_id_boletas": self.contador_id_boletas,
            "contador_id_patrocinadores": self.contador_id_patrocinadores
        }
        with open(RUTA_CONTADORES, 'w') as f_contadores:
            json.dump(contadores, f_contadores)

    def crear_evento_bar(self, id_bar, nombre, fecha, hora_apertura, hora_inicio, lugar, direccion, ciudad, estado,
                         aforo_maximo, porcentaje_ganancias_bar):
        """
        Crea un objeto de evento de bar y devuelve el objeto creado.

        Parameters:
        - id_bar (str): ID del evento de bar.
        - nombre (str): Nombre del evento.
        - fecha (str): Fecha del evento en formato "dd/mm/yyyy".
        - hora_apertura (str): Hora de apertura del evento en formato "HH:MM".
        - hora_inicio (str): Hora de inicio del evento en formato "HH:MM".
        - lugar (str): Lugar del evento.
        - direccion (str): Dirección del lugar del evento.
        - ciudad (str): Ciudad del evento.
        - estado (str): Estado del evento (Por Realizar, Realizado, Cancelado, Aplazado, Cerrado).
        - aforo_maximo (int): Aforo máximo del evento.
        - porcentaje_ganancias_bar (float): Porcentaje de ganancias del bar.

        Returns:
        - objeto_bar (Bar): Objeto de evento de bar creado.
        """
        objeto_bar = Bar(id_bar, nombre, fecha, hora_apertura, hora_inicio, lugar, direccion, ciudad, estado,
                         aforo_maximo, porcentaje_ganancias_bar)
        self.contador_id_eventos += 1
        return objeto_bar

    def crear_evento_teatro(self, id_teatro, nombre, fecha, hora_apertura, hora_inicio, lugar, direccion,
                            ciudad, estado, aforo_maximo, alquiler_teatro):
        """
        Crea un objeto de evento de teatro y devuelve el objeto creado.

        Parameters:
        - id_teatro (str): ID del evento de teatro.
        - nombre (str): Nombre del evento.
        - fecha (str): Fecha del evento en formato "dd/mm/yyyy".
        - hora_apertura (str): Hora de apertura del evento en formato "HH:MM".
        - hora_inicio (str): Hora de inicio del evento en formato "HH:MM".
        - lugar (str): Lugar del evento.
        - direccion (str): Dirección del lugar del evento.
        - ciudad (str): Ciudad del evento.
        - estado (str): Estado del evento (Por Realizar, Realizado, Cancelado, Aplazado, Cerrado).
        - aforo_maximo (int): Aforo máximo del evento.
        - alquiler_teatro (float): Costo del alquiler del teatro.

        Returns:
        - objeto_teatro (Teatro): Objeto de evento de teatro creado.
        """
        objeto_teatro = Teatro(id_teatro, nombre, fecha, hora_apertura, hora_inicio, lugar, direccion, ciudad, estado,
                               aforo_maximo, alquiler_teatro)
        self.contador_id_eventos += 1
        return objeto_teatro

    def crear_evento_filantropico(self, id_filantropico, nombre, fecha, hora_apertura, hora_show, lugar,
                                  direccion, ciudad, estado, aforo_maximo):
        """
        Crea un objeto de evento filantrópico y devuelve el objeto creado.

        Parameters:
        - id_filantropico (str): ID del evento filantrópico.
        - nombre (str): Nombre del evento.
        - fecha (str): Fecha del evento en formato "dd/mm/yyyy".
        - hora_apertura (str): Hora de apertura del evento en formato "HH:MM".
        - hora_show (str): Hora de inicio del show en formato "HH:MM".
        - lugar (str): Lugar del evento.
        - direccion (str): Dirección del lugar del evento.
        - ciudad (str): Ciudad del evento.
        - estado (str): Estado del evento (Por Realizar, Realizado, Cancelado, Aplazado, Cerrado).
        - aforo_maximo (int): Aforo máximo del evento.

        Returns:
        - objeto_filantropico (Filantropico): Objeto de evento filantrópico creado.
        """
        objeto_filantropico = Filantropico(id_filantropico, nombre, fecha, hora_apertura, hora_show, lugar,
                                           direccion, ciudad, estado, aforo_maximo,)
        self.contador_id_eventos += 1
        return objeto_filantropico

    def agregar_evento_objeto(self, objeto_evento):
        """
        Agrega un objeto de evento a la lista de eventos y guarda la lista actualizada en el archivo correspondiente.

        Parameters:
        - objeto_evento: Objeto de evento a agregar.

        Raises:
        - ValueError: Si el objeto no es una instancia de Evento.
        """
        if isinstance(objeto_evento, Evento):
            self.eventos.append(objeto_evento.__dict__)
            with open(RUTA_EVENTOS, "w") as f:
                json.dump(self.eventos, f, indent=4)
            st.balloons()
        else:
            raise ValueError("El objetno no es instancia de Evento, no se añade a la lista de Eventos")

    def buscar_evento_id(self, evento_id):
        """
        Busca un evento por su ID en el archivo de eventos y devuelve el evento encontrado.

        Parameters:
        - evento_id (str): ID del evento a buscar.

        Returns:
        - evento (dict): Diccionario que representa el evento encontrado.

        Raises:
        - KeyError: Si el evento no fue encontrado.
        """
        with open(RUTA_EVENTOS, "r") as f_eventos_leer:
            eventos = json.load(f_eventos_leer)
            for evento in eventos:
                if evento.get("id_evento") == evento_id:
                    return evento
            raise KeyError("El Evento no fue Encontrado")

    def crear_boleta_bar(self, id_boleta_bar, medio_pago, precio_estandar, precio_preventa,
                         porcentaje_descuento, es_cortesia):
        """
        Crea un objeto de BoletaBar y devuelve el objeto creado.

        Parameters:
        - id_boleta_bar (str): ID de la boleta para el bar.
        - medio_pago (str): Método de pago utilizado para la compra de la boleta.
        - precio_estandar (float): Precio estándar de la boleta.
        - precio_preventa (float): Precio de preventa de la boleta.
        - porcentaje_descuento (float): Porcentaje de descuento aplicado a la boleta.
        - es_cortesia (bool): Indica si la boleta es una cortesía.

        Returns:
        - objeto_boleta_bar (BoletaBar): Objeto de BoletaBar creado.
        """
        objeto_boleta_bar = BoletaBar(id_boleta_bar, medio_pago, precio_estandar, precio_preventa,
                                      porcentaje_descuento, es_cortesia)
        self.contador_id_boletas += 1
        return objeto_boleta_bar

    def crear_boleta_filantropico(self, id_boleta_filantropico, medio_pago, precio_estandar,
                                  precio_preventa, porcentaje_descuento, es_cortesia):
        """
        Crea un objeto de BoletaFilantropico y devuelve el objeto creado.

        Parameters:
        - id_boleta_filantropico (str): ID de la boleta filantrópica.
        - medio_pago (str): Método de pago utilizado para la compra de la boleta.
        - precio_estandar (float): Precio estándar de la boleta.
        - precio_preventa (float): Precio de preventa de la boleta.
        - porcentaje_descuento (float): Porcentaje de descuento aplicado a la boleta.
        - es_cortesia (bool): Indica si la boleta es una cortesía.

        Returns:
        - objeto_boleta_filantropico (BoletaFilantropico): Objeto de BoletaFilantropico creado.
        """
        objeto_boleta_filantropico = BoletaFilantropico(id_boleta_filantropico, medio_pago, precio_estandar,
                                                        precio_preventa, porcentaje_descuento, es_cortesia)
        self.contador_id_boletas += 1
        return objeto_boleta_filantropico

    def crear_boleta_teatro(self, id_boleta_teatro, medio_pago, precio_estandar,
                            precio_preventa, porcentaje_descuento, es_cortesia):
        """
        Crea un objeto de BoletaTeatro y devuelve el objeto creado.

        Parameters:
        - id_boleta_teatro (str): ID de la boleta de teatro.
        - medio_pago (str): Método de pago utilizado para la compra de la boleta.
        - precio_estandar (float): Precio estándar de la boleta.
        - precio_preventa (float): Precio de preventa de la boleta.
        - porcentaje_descuento (float): Porcentaje de descuento aplicado a la boleta.
        - es_cortesia (bool): Indica si la boleta es una cortesía.

        Returns:
        - objeto_boleta_teatro (BoletaTeatro): Objeto de BoletaTeatro creado.
        """
        objeto_boleta_teatro = BoletaTeatro(id_boleta_teatro, medio_pago, precio_estandar,
                                            precio_preventa, porcentaje_descuento, es_cortesia)
        self.contador_id_boletas += 1
        return objeto_boleta_teatro

    def agregar_boleta_a_evento(self, evento_id, diccionario_boleta, boleta_id):
        """
        Agrega una boleta a un evento específico.

        Parameters:
        - evento_id (str): ID del evento al que se agregará la boleta.
        - diccionario_boleta (dict): Diccionario con la información de la boleta a agregar.
        - boleta_id (str): ID de la boleta.

        Raises:
        - ValueError: Si el evento ya ha sido realizado.
        """
        with open(RUTA_EVENTOS, "r") as f:
            eventos = json.load(f)
        for evento in eventos:
            if evento.get("id_evento") == evento_id:
                if evento['estado'] == "Realizado":
                    st.warning("El evento ya fue Realizado, No se pueden realizar cambios")
                    return
                if "boletas" not in evento:
                    evento["boletas"] = {}

                if diccionario_boleta["tipo_boleta"] == "Bar" and evento["tipo"] == "Bar":
                    diccionario_boleta["porcentaje_ganancias_boleteria"] = evento.get("porcentaje_ganancias_boleteria")

                evento["boletas"][diccionario_boleta["id_boleta"]] = diccionario_boleta

                with open(RUTA_EVENTOS, "w") as f:
                    json.dump(eventos, f, indent=4)
                    st.snow()
                break
        # r+ es modo de lectura y escritura
        with open(RUTA_BOLETAS, "r+") as f_boletas:
            boletas = json.load(f_boletas)
            for boleta in boletas:
                if boleta.get("id_boleta") == boleta_id:
                    if diccionario_boleta["tipo_boleta"] == "Bar" and evento["tipo"] == "Bar":
                        boleta["porcentaje_ganancias_boleteria"] = evento.get("porcentaje_ganancias_boleteria")
                    f_boletas.seek(0)
                    json.dump(boletas, f_boletas, indent=4)
                    f_boletas.truncate()
                    break

    def agregar_boleta_objeto(self, objeto_boleta):
        """
        Agrega una boleta al sistema.

        Parameters:
        - objeto_boleta (Boleta): Instancia del objeto Boleta a agregar.

        Raises:
        - ValueError: Si el objeto no es una instancia de Boleta.

        """
        if isinstance(objeto_boleta, Boleta):
            self.boletas.append(objeto_boleta.__dict__)
            with open(RUTA_BOLETAS, "w") as f:
                json.dump(self.boletas, f, indent=4)
            st.balloons()
        else:
            raise ValueError("El objeto no es instancia de Boleta, no se añade a la lista de Eventos")

    def buscar_boleta_id(self, boleta_id):
        """
         Busca una boleta por su ID.

         Parameters:
         - boleta_id (str): ID de la boleta a buscar.

         Returns:
         - dict: Diccionario con la información de la boleta.

         Raises:
         - KeyError: Si la boleta no se encuentra.

         """
        with open(RUTA_BOLETAS, "r") as f_boletas_leer:
            boletas = json.load(f_boletas_leer)
            for boleta in boletas:
                if boleta.get("id_boleta") == boleta_id:
                    return boleta
            raise KeyError("La Boleta no fue Encontrada")

    def agregar_usuario_a_boleta(self, nombre_usuario, documento_usuario, correo_usuario, medio_enterado, boleta_id,
                                 tipo_venta):
        """
        Agrega información de usuario a una boleta y marca la boleta como vendida.

        Parameters:
        - nombre_usuario (str): Nombre del usuario.
        - documento_usuario (str): Documento del usuario.
        - correo_usuario (str): Correo del usuario.
        - medio_enterado (str): Medio por el cual se enteró el usuario del evento.
        - boleta_id (str): ID de la boleta a la que se le agregará la información.
        - tipo_venta (str): Tipo de venta de la boleta.

        Returns:
        - None

        """
        with open(RUTA_EVENTOS, "r+") as f_eventos:
            eventos = json.load(f_eventos)
            for evento in eventos:
                boletas = evento['boletas']
                for boleta_key, boleta_info in boletas.items():
                    if boleta_info['id_boleta'] == boleta_id and evento['aforo_vendido'] < evento['aforo_max']:
                        boleta_info['nombre_usuario'] = nombre_usuario
                        boleta_info['documento_usuario'] = documento_usuario
                        boleta_info['correo_usuario'] = correo_usuario
                        boleta_info['medio_enterado'] = medio_enterado
                        boleta_info['vendida'] = True
                        boleta_info['tipo_venta'] = tipo_venta
                        evento['aforo_vendido'] += 1
                        f_eventos.seek(0)
                        json.dump(eventos, f_eventos, indent=4)
                        f_eventos.truncate()
                        st.snow()
                        break

        with open(RUTA_BOLETAS, "r+") as f_boletas:
            boletas = json.load(f_boletas)
            for boleta in boletas:
                if boleta.get("id_boleta") == boleta_id:
                    boleta['nombre_usuario'] = nombre_usuario
                    boleta['documento_usuario'] = documento_usuario
                    boleta['correo_usuario'] = correo_usuario
                    boleta['medio_enterado'] = medio_enterado
                    boleta['vendida'] = True
                    boleta['tipo_venta'] = tipo_venta
                    f_boletas.seek(0)
                    json.dump(boletas, f_boletas, indent=4)
                    f_boletas.truncate()
                    st.balloons()
                    break

    def generar_boleta_pdf(self, diccionario_boleta):
        """
        Genera un archivo PDF con la información de una boleta.

        Parameters:
        - diccionario_boleta (dict): Diccionario que contiene la información de la boleta.

        Returns:
        - None

        """
        doc = SimpleDocTemplate(RUTA_PDF_GENERADO, pagesize=letter)
        styles = getSampleStyleSheet()
        estilo_normal = styles['Normal']
        contenido = []
        contenido.append(Paragraph(FECHA_ACTUAL, estilo_normal))
        imagen_superior = RUTA_LOGO
        imagen_superior = Image(imagen_superior, width=letter[0], height=400)
        contenido.append(imagen_superior)
        for clave, valor in diccionario_boleta.items():
            contenido.append(Paragraph(f"<b>{clave}</b>: {valor}", estilo_normal))
        imagen_inferior = RUTA_QR
        imagen_inferior = Image(imagen_inferior, width=letter[0], height=400)
        contenido.append(imagen_inferior)
        doc.build(contenido)

    def crear_artista_objeto(self, id_artista, nombre_artista, pago_artista):
        """
        Crea un objeto de tipo Artista.

        Parameters:
        - id_artista (str): ID del artista.
        - nombre_artista (str): Nombre del artista.
        - pago_artista (int): Cobro del artista.

        Returns:
        - objeto_artista (Artista): Objeto de tipo Artista creado.

        """
        objeto_artista = Artista(id_artista, nombre_artista, pago_artista)
        self.contador_id_artistas += 1
        return objeto_artista

    def agregar_artista_objeto(self, objeto_artista):
        """
        Agrega un objeto artista a la lista de artistas y guarda la información en el archivo correspondiente.

        Parameters:
        - objeto_artista (Artista): Objeto Artista a agregar.

        Raises:
        - ValueError: Si el objeto no es instancia de Artista.

        """
        if isinstance(objeto_artista, Artista):
            self.artistas.append(objeto_artista.__dict__)
            with open(RUTA_ARTISTAS, "w") as f:
                json.dump(self.artistas, f, indent=4)
            st.balloons()
        else:
            raise ValueError("El objeto no es instancia de Artista, no se añade a la lista de Artistas")

    def buscar_artista_id(self, artista_id):
        """
        Busca un artista por su ID en el archivo de artistas.

        Parameters:
        - artista_id (str): ID del artista a buscar.

        Returns:
        - dict: Diccionario con la información del artista encontrado.

        Raises:
        - KeyError: Si el artista con el ID especificado no fue encontrado.

        """
        with open(RUTA_ARTISTAS, "r") as f_artistas_leer:
            artistas = json.load(f_artistas_leer)
            for artista in artistas:
                if artista.get("id_artista") == artista_id:
                    return artista
            raise KeyError("El Artista no fue Encontrado")

    def agregar_artista_a_evento(self, evento_id, diccionario_artista):
        """
        Agrega un artista a un evento.

        Parameters:
        - evento_id (str): ID del evento al que se desea agregar el artista.
        - diccionario_artista (dict): Diccionario con la información del artista a agregar.

        """
        with open(RUTA_EVENTOS, "r") as f:
            eventos = json.load(f)
        for evento in eventos:
            if evento.get("id_evento") == evento_id:
                if evento['estado'] == "Realizado":
                    st.warning("El evento ya fue Realizado, No se permiten Cambios")
                    return
                if "artistas" not in evento:
                    evento["artistas"] = {}

                evento["artistas"][diccionario_artista["id_artista"]] = diccionario_artista

                with open(RUTA_EVENTOS, "w") as f:
                    json.dump(eventos, f, indent=4)
                    st.snow()
                break

    def crear_patrocinador_objeto(self, id_patrocinador, nombre, apoyo):
        """
        Crea un objeto patrocinador.

        Parameters:
        - id_patrocinador (str): ID del patrocinador.
        - nombre (str): Nombre del patrocinador.
        - apoyo (str): Tipo de apoyo del patrocinador.

        Returns:
        - Patrocinador: Objeto de la clase Patrocinador creado.

        """
        objeto_patrocinador = Patrocinador(id_patrocinador, nombre, apoyo)
        self.contador_id_patrocinadores += 1
        return objeto_patrocinador

    def agregar_patrocinador_objeto(self, objeto_patrocinador):
        """
        Agrega un objeto patrocinador al archivo de patrocinadores.

        Parameters:
        - objeto_patrocinador (Patrocinador): Objeto de la clase Patrocinador a agregar.

        Raises:
        - ValueError: Si el objeto no es una instancia de Patrocinador.
        """
        if isinstance(objeto_patrocinador, Patrocinador):
            self.patrocinadores.append(objeto_patrocinador.__dict__)
            with open(RUTA_PATROCINADORES, "w") as f:
                json.dump(self.patrocinadores, f, indent=4)
            st.balloons()
        else:
            raise ValueError("El objeto no es instancia de Patrocinadores, no se añade a la lista de Patrocinadores")

    def buscar_patrocinador_id(self, patrocinador_id):
        """
        Busca un patrocinador por su identificador en el archivo de patrocinadores.

        Parameters:
        - patrocinador_id (str): Identificador del patrocinador a buscar.

        Returns:
        - dict: Diccionario con la información del patrocinador encontrado.

        Raises:
        - KeyError: Si el patrocinador no se encuentra en el archivo.
        """
        with open(RUTA_PATROCINADORES, "r") as f_patrocinadores_leer:
            patrocinadores = json.load(f_patrocinadores_leer)
            for patrocinador in patrocinadores:
                if patrocinador.get("id_patrocinador") == patrocinador_id:
                    return patrocinador
            raise KeyError("El Patrocinador no fue Encontrado")

    def agregar_patrocinador_a_evento(self, evento_id, diccionario_patrocinador):
        """
        Agrega un patrocinador al evento correspondiente en el archivo de eventos.

        Parameters:
        - evento_id (str): Identificador del evento al que se desea agregar el patrocinador.
        - diccionario_patrocinador (dict): Diccionario que contiene la información del patrocinador a agregar.

        Raises:
        - ValueError: Si el evento ya está realizado o si el tipo de evento no admite patrocinadores.
        """
        with open(RUTA_EVENTOS, "r") as f:
            eventos = json.load(f)
        for evento in eventos:
            if evento.get("id_evento") == evento_id:
                if evento["estado"] == "Realizado":
                    st.warning("No se pueden agregar patrocinadores a un evento realizado.")
                    return
                if "patrocinadores" not in evento:
                    evento["patrocinadores"] = {}

                if evento["tipo"] == "Filantropico":
                    evento["patrocinadores"][diccionario_patrocinador["id_patrocinador"]] = diccionario_patrocinador
                    with open(RUTA_EVENTOS, "w") as f:
                        json.dump(eventos, f, indent=4)
                        st.snow()
                    break
                else:
                    raise ValueError("El Evento no Admite Patrocinadores")

    def buscar_usuario_ingreso(self, diccionario_evento, usuario_id):
        """
        Busca un usuario en el diccionario de evento para permitir o denegar su ingreso.

        Parameters:
        - diccionario_evento (dict): Diccionario que contiene la información del evento.
        - usuario_id (str): Identificador del usuario a buscar.

        Returns:
        - str: Mensaje indicando si el usuario puede pasar o no.
        """
        if diccionario_evento["boletas"]:
            for boleta_id, boleta_info in diccionario_evento["boletas"].items():
                if boleta_info["documento_usuario"] == usuario_id:
                    st.write("El Usuario Puede Pasar")
                    st.balloons()
                else:
                    st.write("EJECUTENLO!!!")

    def obtener_datos_dashboard_frecuencia(self, fecha_inicio, fecha_fin):
        """
        Obtiene los datos para el dashboard de frecuencia de eventos.

        Parameters:
        - fecha_inicio (str): Fecha de inicio en formato "dd/mm/yyyy".
        - fecha_fin (str): Fecha de fin en formato "dd/mm/yyyy".

        Returns:
        - tuple: Tupla de dos elementos. El primer elemento es una lista de los tipos de eventos.
                 El segundo elemento es un vector numpy con la cantidad de eventos por cada tipo.
        """
        with open(RUTA_EVENTOS, 'r') as archivo:
            eventos = json.load(archivo)

        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        eventos_por_tipo = {}

        for evento in eventos:
            if evento['fecha'] == "NA":
                continue

            fecha_evento = datetime.strptime(evento['fecha'], "%d/%m/%Y")

            if fecha_inicio <= fecha_evento <= fecha_fin:
                tipo_evento = evento['tipo']
                if tipo_evento in eventos_por_tipo:
                    eventos_por_tipo[tipo_evento] += 1
                else:
                    eventos_por_tipo[tipo_evento] = 1

        tipos_evento = list(eventos_por_tipo.keys())
        cantidad_eventos = list(eventos_por_tipo.values())
        vector_cantidad_eventos = np.array(cantidad_eventos)

        return tipos_evento, vector_cantidad_eventos

    def obtener_datos_dashboard_ingresos(self, fecha_inicio, fecha_fin):
        """
        Obtiene los datos para el dashboard de ingresos.

        Parameters:
        - fecha_inicio (str): Fecha de inicio en formato "dd/mm/yyyy".
        - fecha_fin (str): Fecha de fin en formato "dd/mm/yyyy".

        Returns:
        - tuple: Tupla de dos listas. La primera lista contiene los nombres de los eventos
                 y la segunda lista contiene los ingresos asociados a cada evento.
        """
        with open(RUTA_EVENTOS, 'r') as archivo:
            eventos = json.load(archivo)

        nombres_eventos = []
        ingresos_eventos = []

        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")

        for evento in eventos:
            fecha_evento = datetime.strptime(evento['fecha'], "%d/%m/%Y")
            if fecha_inicio <= fecha_evento <= fecha_fin:
                ingresos_evento = 0
                for _, boleta in evento['boletas'].items():
                    if boleta['vendida'] and boleta['es_cortesia'] == 'No':
                        precio = boleta['precio_estandar'] if boleta['tipo_venta'] == 'VentaNormal' else boleta[
                            'precio_preventa']
                        ingresos_evento += precio
                nombres_eventos.append(evento['nombre'])
                ingresos_eventos.append(ingresos_evento)

        return nombres_eventos, ingresos_eventos

    def generar_dashboard(self, datos1, datos2):
        """
        Genera un dashboard con dos gráficos de barras.

        Parameters:
        - datos1 (tuple): Tupla de dos listas. La primera lista contiene los tipos de eventos
                          y la segunda lista contiene la cantidad de eventos por tipo.
        - datos2 (tuple): Tupla de dos listas. La primera lista contiene los nombres de los eventos
                          y la segunda lista contiene los ingresos asociados a cada evento.
        """
        tipos_evento, cantidad_eventos = datos1

        fig1, ax1 = plt.subplots()
        ax1.bar(tipos_evento, cantidad_eventos, color='blue')
        ax1.set_xlabel('Tipo de Evento')
        ax1.set_ylabel('Cantidad de Eventos')
        ax1.set_title('Cantidad de Eventos por Tipo')

        # Datos para el segundo gráfico de barras
        eventos, ingresos = datos2

        fig2, ax2 = plt.subplots()
        ax2.bar(eventos, ingresos, color='green')
        ax2.set_xlabel('Eventos')
        ax2.set_ylabel('Ingresos')
        ax2.set_title('Ingresos por Evento')

        # Mostrar ambos gráficos en Streamlit
        st.pyplot(fig1)
        st.pyplot(fig2)
