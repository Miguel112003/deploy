import streamlit as st
from settings import RUTA_LOGO, CENTRADO_CSS_TEXTO


def dibujar_pagina_inicial(gui_controller):
    """
    Función para dibujar la página inicial de la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    st.sidebar.title("Bienvenido")

    st.markdown(CENTRADO_CSS_TEXTO, unsafe_allow_html=True)
    st.markdown("<h1 class='centrado-texto'>Sistema de Gestión de Eventos Toxicómicos</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.image(RUTA_LOGO)
        opcion = st.selectbox(label="Elija Menu a Consultar", options=['Eventos', 'Boleteria', 'Reportes/Dashboard',
                                                                       'Artistas', 'Patrocinadores', 'Ingreso Evento'])
    if opcion == 'Eventos':
        dibujar_menu_eventos(gui_controller)
    elif opcion == 'Boleteria':
        dibujar_menu_boleteria(gui_controller)
    elif opcion == 'Reportes/Dashboard':
        dibujar_menu_reportes(gui_controller)
    elif opcion == 'Artistas':
        dibujar_menu_artistas(gui_controller)
    elif opcion == 'Patrocinadores':
        dibujar_menu_patrocinadores(gui_controller)
    elif opcion == 'Ingreso Evento':
        dibujar_menu_ingreso_evento(gui_controller)


def dibujar_menu_eventos(gui_controller):
    """
    Función para dibujar el menú de gestión de eventos en la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    with st.sidebar:
        opcion_eventos = st.selectbox(label="Elija que Desea Realizar en Eventos", options=['Crear', 'Mostrar por ID'])
    if opcion_eventos == 'Crear':
        with st.sidebar:
            tipo_evento = st.selectbox(label="Elija que Tipo de evento va a Crear", options=['Bar',
                                                                                             'Teatro', 'Filantropico'])
        nombre = col_izq.text_input('Nombre del Evento', placeholder='No me Graduo en Septiembre')
        id = str(gui_controller.sistema_gestion.contador_id_eventos)
        col_der.write(f"ID del Evento: {gui_controller.sistema_gestion.contador_id_eventos}")
        fecha = col_izq.text_input('Fecha del Evento', placeholder='24/05/2024')
        hora_apertura = col_der.text_input('Hora de Apertura', placeholder='22:00')
        hora_inicio = col_izq.text_input('Hora de Inicio', placeholder='22:30')
        lugar = col_der.text_input('Lugar', placeholder='Teatro Jorgito')
        direccion = col_izq.text_input('Direccion', placeholder='Calle 14c #99-33')
        ciudad = col_der.text_input('Ciudad', placeholder='Cali')
        estado = col_izq.selectbox(label='Estado', options=['Por Realizar', 'Realizado', 'Cancelado',
                                                            'Aplazado', 'Cerrado'])
        aforo_maximo = col_der.number_input('Aforo maximo', placeholder='100', step=1)

        if tipo_evento == 'Bar':
            porcentaje_ganancias_bar = col_izq.number_input('Porcentaje de ganancias del Bar', placeholder='70')
            if (nombre != '' and fecha != '' and hora_apertura != '' and hora_inicio != '' and
                    lugar != '' and direccion != '' and ciudad != '' and estado != '' and aforo_maximo > 0
                    and 0 < porcentaje_ganancias_bar < 100):
                with st.sidebar:
                    boton_crear = st.button('Crear Evento')
                    if boton_crear:
                        objeto_creado = gui_controller.sistema_gestion.crear_evento_bar(id, nombre, fecha,
                                                                                        hora_apertura, hora_inicio,
                                                                                        lugar, direccion, ciudad,
                                                                                        estado, aforo_maximo,
                                                                                        porcentaje_ganancias_bar)
                        gui_controller.sistema_gestion.agregar_evento_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()

        elif tipo_evento == 'Teatro':
            alquiler_teatro = col_izq.number_input('Costo del Alquiler del Teatro', placeholder='120.000')
            if (nombre != '' and fecha != '' and hora_apertura != '' and hora_inicio != '' and
                    lugar != '' and direccion != '' and ciudad != '' and estado != '' and aforo_maximo > 0
                    and 0 < alquiler_teatro):
                with st.sidebar:
                    boton_crear = st.button('Crear Evento')
                    if boton_crear:
                        objeto_creado = gui_controller.sistema_gestion.crear_evento_teatro(id, nombre, fecha,
                                                                                           hora_apertura, hora_inicio,
                                                                                           lugar, direccion, ciudad,
                                                                                           estado, aforo_maximo,
                                                                                           alquiler_teatro)
                        gui_controller.sistema_gestion.agregar_evento_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()
        elif tipo_evento == 'Filantropico':
            if (nombre != '' and fecha != '' and hora_apertura != '' and hora_inicio != '' and
                    lugar != '' and direccion != '' and ciudad != '' and estado != '' and aforo_maximo > 0):
                with st.sidebar:
                    boton_crear = st.button('Crear Evento')
                    if boton_crear:
                        objeto_creado = gui_controller.sistema_gestion.crear_evento_filantropico(id, nombre, fecha,
                                                                                                 hora_apertura,
                                                                                                 hora_inicio, lugar,
                                                                                                 direccion, ciudad,
                                                                                                 estado, aforo_maximo)
                        gui_controller.sistema_gestion.agregar_evento_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()

    elif opcion_eventos == 'Mostrar por ID':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda = st.text_input('ID de Evento a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            evento_encontrado = gui_controller.sistema_gestion.buscar_evento_id(id_busqueda)
            mostrar_informacion_evento(evento_encontrado)


def dibujar_menu_boleteria(gui_controller):
    """
     Función para dibujar el menú de gestión de boletería en la interfaz de usuario.

     Parameters:
     - gui_controller (GuiController): El controlador de la interfaz de usuario.

     Returns:
     - None
     """
    col_izq, col_der = st.columns(2)
    with st.sidebar:
        opcion_boleteria = st.selectbox(label="Elija que Desea Realizar en Boleteria", options=['Crear Boleta',
                                                                                                'Agregar a Evento',
                                                                                                'Mostrar por ID',
                                                                                                'PDF por ID',
                                                                                                'Vender a Usuario'])
    if opcion_boleteria == 'Vender a Usuario':
        busqueda_realizada = False
        nombre_usuario = col_izq.text_input('Nombre del Usuario', placeholder="Miguelito el que se no graduara solo "
                                                                              "porque no terminara la tesis por este"
                                                                              " proyecto")
        documento_usuario = col_der.text_input('Documento del Usuario', placeholder="1005555555")
        correo_usuario = col_izq.text_input('Correo del Usuario', placeholder="jhondoe@gmail.com")
        medio_enterado = col_der.selectbox(label="Medio de enterado del Usuario",
                                           options=['Redes Sociales',
                                                    'Amigos/Familia',
                                                    'Medios Impresos',
                                                    'Pagina Web'])
        tipo_venta = col_izq.selectbox(label="Tipo de Venta", options=['Preventa', 'Venta Estandar'])
        venta_lista = st.checkbox("Venta")
        with st.sidebar:
            id_busqueda = st.text_input('ID de Boleta a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    boleta_encontrada = gui_controller.sistema_gestion.buscar_boleta_id(id_busqueda)
                    mostrar_informacion_boleta(boleta_encontrada)
                    busqueda_realizada = True
                    if (nombre_usuario != '' and correo_usuario != '' and medio_enterado != ''
                            and documento_usuario != '' and tipo_venta != '' and venta_lista):
                        gui_controller.sistema_gestion.agregar_usuario_a_boleta(nombre_usuario, documento_usuario,
                                                                                correo_usuario, medio_enterado,
                                                                                id_busqueda,
                                                                                tipo_venta)
        st.write("Si es el evento que esta buscando, vuelva a presionar Buscar pero con el checkbox marcado")

    elif opcion_boleteria == 'Crear Boleta':
        with st.sidebar:
            tipo_boleta = st.selectbox('Tipo de Boleta', options=['Bar', 'Teatro', 'Filantropico'])

        id = str(gui_controller.sistema_gestion.contador_id_boletas)
        col_der.write(f"ID de la Boleta: {gui_controller.sistema_gestion.contador_id_boletas}")
        medio_pago = col_izq.selectbox(label='Medio de Pago', options=['Tarjeta', 'Otros Medios'])

        if tipo_boleta == 'Filantropico':
            precio_estandar = 0
            precio_preventa = 0
            porcentaje_descuento = 100
            es_cortesia = 'Si'
            col_der.write('Precio Estandar: 0')
            col_izq.write('Precio Preventa: 0')
            col_der.write('Porcentaje Descuento:0')
            col_izq.write('Cortesia: Si')
            if medio_pago != '':
                with st.sidebar:
                    boton_crear_boleta = st.button('Crear Boleta')
                    if boton_crear_boleta:
                        objeto_creado = gui_controller.sistema_gestion.crear_boleta_filantropico(id, medio_pago,
                                                                                                 precio_estandar,
                                                                                                 precio_preventa,
                                                                                                 porcentaje_descuento,
                                                                                                 es_cortesia)
                        gui_controller.sistema_gestion.agregar_boleta_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()

        elif tipo_boleta == 'Bar':
            precio_estandar = col_der.number_input('Precio Estandar', placeholder='130000')
            precio_preventa = col_izq.number_input('Precio Preventa', placeholder='120000')
            porcentaje_descuento = col_der.number_input('Porcentaje Descuento', placeholder='5')
            es_cortesia = col_izq.selectbox(label='Es Cortesia', options=['Si', 'No'])
            if precio_estandar != '' and precio_preventa != '' and porcentaje_descuento != '' and es_cortesia != '':
                with st.sidebar:
                    boton_crear_boleta = st.button('Crear Boleta')
                    if boton_crear_boleta:
                        objeto_creado = gui_controller.sistema_gestion.crear_boleta_bar(id, medio_pago, precio_estandar,
                                                                                        precio_preventa,
                                                                                        porcentaje_descuento,
                                                                                        es_cortesia)
                        gui_controller.sistema_gestion.agregar_boleta_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()

        elif tipo_boleta == 'Teatro':
            precio_estandar = col_der.number_input('Precio Estandar', placeholder='130000')
            precio_preventa = col_izq.number_input('Precio Preventa', placeholder='120000')
            porcentaje_descuento = col_der.number_input('Porcentaje Descuento', placeholder='5')
            es_cortesia = col_izq.selectbox(label='Es Cortesia', options=['Si', 'No'])
            if precio_estandar != '' and precio_preventa != '' and porcentaje_descuento != '' and es_cortesia != '':
                with st.sidebar:
                    boton_crear_boleta = st.button('Crear Boleta')
                    if boton_crear_boleta:
                        objeto_creado = gui_controller.sistema_gestion.crear_boleta_teatro(id, medio_pago,
                                                                                           precio_estandar,
                                                                                           precio_preventa,
                                                                                           porcentaje_descuento,
                                                                                           es_cortesia)
                        gui_controller.sistema_gestion.agregar_boleta_objeto(objeto_creado)
                        gui_controller.sistema_gestion.guardar_contadores()

    elif opcion_boleteria == 'Mostrar por ID':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda = st.text_input('ID de Boleta a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            boleta_encontrada = gui_controller.sistema_gestion.buscar_boleta_id(id_busqueda)
            mostrar_informacion_boleta(boleta_encontrada)

    elif opcion_boleteria == 'PDF por ID':
        with st.sidebar:
            id_busqueda = st.text_input('ID de Boleta a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    boleta_encontrada = gui_controller.sistema_gestion.buscar_boleta_id(id_busqueda)
                    if boleta_encontrada['vendida']:
                        mostrar_informacion_boleta(boleta_encontrada)
                        gui_controller.sistema_gestion.generar_boleta_pdf(boleta_encontrada)
                        st.write("La boleta fue generada con Exito, revise el directorio")
                    else:
                        raise ValueError("La Boleta no ha Sido Vendida, No Generare un PDF para nada")

    elif opcion_boleteria == 'Agregar a Evento':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda_evento = st.text_input('ID del Evento a Buscar', placeholder='123456789')
            id_busqueda_boleta = st.text_input('ID de la Boleta a Buscar', placeholder='123456789')
            if id_busqueda_evento != '' and id_busqueda_boleta != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            boleta_encontrada = gui_controller.sistema_gestion.buscar_boleta_id(id_busqueda_boleta)
            gui_controller.sistema_gestion.agregar_boleta_a_evento(id_busqueda_evento,
                                                                   boleta_encontrada, id_busqueda_boleta)


def dibujar_menu_artistas(gui_controller):
    """
    Función para dibujar el menú de gestión de artistas en la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    with st.sidebar:
        opcion_artistas = st.selectbox(label="Elija que Desea Realizar en Artistas",
                                       options=['Crear Artista',
                                                'Mostrar Artista por ID',
                                                'Agregar Artista a Evento'])

    if opcion_artistas == 'Crear Artista':
        id_artista = str(gui_controller.sistema_gestion.contador_id_artistas)
        col_izq.write(f"ID del Artista: {gui_controller.sistema_gestion.contador_id_artistas}")
        nombre_artista = col_der.text_input('Nombre del Artista', placeholder='Gonzalo Noreña')
        pago_artista = col_izq.number_input('Cobro del Artista', placeholder='130000')
        if id_artista != '' and nombre_artista != '' and pago_artista != '':
            with st.sidebar:
                boton_crear_artista = st.button('Crear Artista')
                if boton_crear_artista:
                    objeto_creado = gui_controller.sistema_gestion.crear_artista_objeto(id_artista,
                                                                                        nombre_artista, pago_artista)
                    gui_controller.sistema_gestion.agregar_artista_objeto(objeto_creado)
                    gui_controller.sistema_gestion.guardar_contadores()

    elif opcion_artistas == 'Mostrar Artista por ID':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda = st.text_input('ID de Artista a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            artista_encontrado = gui_controller.sistema_gestion.buscar_artista_id(id_busqueda)
            mostrar_informacion_artista(artista_encontrado)

    elif opcion_artistas == 'Agregar Artista a Evento':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda_evento = st.text_input('ID del Evento a Buscar', placeholder='123456789')
            id_busqueda_artista = st.text_input('ID del Artista a Buscar', placeholder='123456789')
            if id_busqueda_evento != '' and id_busqueda_artista != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            artista_encontrado = gui_controller.sistema_gestion.buscar_artista_id(id_busqueda_artista)
            gui_controller.sistema_gestion.agregar_artista_a_evento(id_busqueda_evento, artista_encontrado)


def dibujar_menu_patrocinadores(gui_controller):
    """
    Función para dibujar el menú de gestión de patrocinadores en la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    with st.sidebar:
        opcion_patrocinadores = st.selectbox(label="Elija que Desea Realizar en Patrocinadores",
                                             options=['Crear Patrocinador',
                                                      'Mostrar Patrocinador por ID',
                                                      'Agregar a Evento Filantropico'])

    if opcion_patrocinadores == 'Crear Patrocinador':
        id_patrocinador = str(gui_controller.sistema_gestion.contador_id_patrocinadores)
        col_izq.write(f"ID del Patrocinador: {gui_controller.sistema_gestion.contador_id_patrocinadores}")
        nombre_patrocinador = col_der.text_input('Nombre del Patrocinador', placeholder='Federico el Falso')
        aporte_patrocinador = col_izq.number_input('Aporte del Patrocinador', placeholder='130000')
        if id_patrocinador != '' and nombre_patrocinador != '' and aporte_patrocinador != '':
            with st.sidebar:
                boton_crear_patrocinador = st.button('Crear Patrocinador')
                if boton_crear_patrocinador:
                    objeto_creado = gui_controller.sistema_gestion.crear_patrocinador_objeto(id_patrocinador,
                                                                                             nombre_patrocinador,
                                                                                             aporte_patrocinador)
                    gui_controller.sistema_gestion.agregar_patrocinador_objeto(objeto_creado)
                    gui_controller.sistema_gestion.guardar_contadores()

    elif opcion_patrocinadores == 'Mostrar Patrocinador por ID':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda = st.text_input('ID de Patrocinador a Buscar', placeholder='123456789')
            if id_busqueda != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            patrocinador_encontrado = gui_controller.sistema_gestion.buscar_patrocinador_id(id_busqueda)
            mostrar_informacion_patrocinador(patrocinador_encontrado)

    elif opcion_patrocinadores == 'Agregar a Evento Filantropico':
        variable_de_cambio = False
        with st.sidebar:
            id_busqueda_evento = st.text_input('ID del Evento a Buscar', placeholder='123456789')
            id_busqueda_patrocinador = st.text_input('ID del Patrocinador a Buscar', placeholder='123456789')
            if id_busqueda_evento != '' and id_busqueda_patrocinador != '':
                boton_buscar = st.button('Buscar')
                if boton_buscar:
                    variable_de_cambio = True
        if variable_de_cambio:
            patrocinador_encontrado = gui_controller.sistema_gestion.buscar_patrocinador_id(id_busqueda_patrocinador)
            gui_controller.sistema_gestion.agregar_patrocinador_a_evento(id_busqueda_evento, patrocinador_encontrado)


def dibujar_menu_reportes(gui_controller):
    """
    Función para dibujar el menú de reportes en la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    with st.sidebar:
        opcion_reportes = st.selectbox(label="Elija que Desea Realizar en Reportes",
                                       options=['Generar Reporte de Ventas de Boletas Totales',
                                                'Generar Reporte de Ingresos segun Clasificacion',
                                                'Generar Reporte de Compradores',
                                                'Generar Reporte de Artistas',
                                                'Ver Dashboard'])

    if opcion_reportes == 'Generar Reporte de Ventas de Boletas Totales':
        pass

    elif opcion_reportes == 'Generar Reporte de Ingresos segun Clasificacion':
        pass

    elif opcion_reportes == 'Generar Reporte de Compradores':
        pass

    elif opcion_reportes == 'Generar Reporte de Artistas':
        pass

    elif opcion_reportes == 'Ver Dashboard':
        variable_de_cambio = False
        with st.sidebar:
            fecha_inicial = st.text_input("Fecha de Inicio", placeholder="31/12/2024")
            fecha_final = st.text_input("Fecha Final", placeholder="31/12/2025")
            generar_dashboard = st.button("Generar Dashboard")
            if generar_dashboard and fecha_inicial != '' and fecha_final != '':
                variable_de_cambio = True

        if variable_de_cambio:
            datos1 = gui_controller.sistema_gestion.obtener_datos_dashboard_frecuencia(fecha_inicial, fecha_final)
            datos2 = gui_controller.sistema_gestion.obtener_datos_dashboard_ingresos(fecha_inicial, fecha_final)
            gui_controller.sistema_gestion.generar_dashboard(datos1, datos2)


def dibujar_menu_ingreso_evento(gui_controller):
    """
    Función para dibujar el menú de ingreso de evento en la interfaz de usuario.

    Parameters:
    - gui_controller (GuiController): El controlador de la interfaz de usuario.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    variable_de_cambio = False
    with st.sidebar:
        id_busqueda_evento = st.text_input('ID del Evento a Buscar', placeholder='123456789')
        id_busqueda_usuario = st.text_input('Documento del Usuario', placeholder='123456789')
        if id_busqueda_evento != '' and id_busqueda_usuario != '':
            boton_buscar = st.button('Buscar')
            if boton_buscar:
                variable_de_cambio = True
    if variable_de_cambio:
        evento_encontrado = gui_controller.sistema_gestion.buscar_evento_id(id_busqueda_evento)
        gui_controller.sistema_gestion.buscar_usuario_ingreso(evento_encontrado, id_busqueda_usuario)


def mostrar_informacion_evento(objeto_evento):
    """
    Función para mostrar información de un evento en la interfaz de usuario.

    Parameters:
    - objeto_evento (dict): Un diccionario que contiene la información del evento
                            con claves 'nombre', 'id_evento', 'fecha', 'hora_apertura',
                            'hora_show', 'lugar', 'direccion', 'estado', 'aforo_max',
                            'porcentaje_ganancias_bar', 'tipo' y 'alquiler' (opcional).

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    if objeto_evento["tipo"] == "Bar":
        col_izq.write(f'Nombre del Evento: {objeto_evento["nombre"]}')
        col_der.write(f'Id del Evento: {objeto_evento["id_evento"]}')
        col_izq.write(f'Fecha del Evento: {objeto_evento["fecha"]}')
        col_der.write(f'Hora de Apertura: {objeto_evento["hora_apertura"]}')
        col_izq.write(f'Hora del Show: {objeto_evento["hora_show"]}')
        col_der.write(f'Lugar: {objeto_evento["lugar"]}')
        col_izq.write(f'Direccion: {objeto_evento["direccion"]}')
        col_der.write(f'Estado: {objeto_evento["estado"]}')
        col_izq.write(f'Aforo Maximo: {objeto_evento["aforo_max"]}')
        col_izq.write(f'Porcentaje Ganancias Bar: {objeto_evento["porcentaje_ganancias_bar"]}')
        col_der.write(f'Tipo de Evento: {objeto_evento["tipo"]}')

    elif objeto_evento["tipo"] == "Teatro":
        col_izq.write(f'Nombre del Evento: {objeto_evento["nombre"]}')
        col_der.write(f'Id del Evento: {objeto_evento["id_evento"]}')
        col_izq.write(f'Fecha del Evento: {objeto_evento["fecha"]}')
        col_der.write(f'Hora de Apertura: {objeto_evento["hora_apertura"]}')
        col_izq.write(f'Hora del Show: {objeto_evento["hora_show"]}')
        col_der.write(f'Lugar: {objeto_evento["lugar"]}')
        col_izq.write(f'Direccion: {objeto_evento["direccion"]}')
        col_der.write(f'Estado: {objeto_evento["estado"]}')
        col_izq.write(f'Aforo Maximo: {objeto_evento["aforo_max"]}')
        col_der.write(f'Tipo de Evento: {objeto_evento["tipo"]}')
        col_izq.write(f'Alquiler Teatro: {objeto_evento["alquiler"]}')

    elif objeto_evento["tipo"] == "Filantropico":
        col_izq.write(f'Nombre del Evento: {objeto_evento["nombre"]}')
        col_der.write(f'Id del Evento: {objeto_evento["id_evento"]}')
        col_izq.write(f'Fecha del Evento: {objeto_evento["fecha"]}')
        col_der.write(f'Hora de Apertura: {objeto_evento["hora_apertura"]}')
        col_izq.write(f'Hora del Show: {objeto_evento["hora_show"]}')
        col_der.write(f'Lugar: {objeto_evento["lugar"]}')
        col_izq.write(f'Direccion: {objeto_evento["direccion"]}')
        col_der.write(f'Estado: {objeto_evento["estado"]}')
        col_izq.write(f'Aforo Maximo: {objeto_evento["aforo_max"]}')
        col_der.write(f'Tipo de Evento: {objeto_evento["tipo"]}')


def mostrar_informacion_boleta(objeto_boleta):
    """
    Función para mostrar información de una boleta en la interfaz de usuario.

    Parameters:
    - objeto_boleta (dict): Un diccionario que contiene la información de la boleta
                            con claves 'id_boleta', 'medio_pago', 'precio_estandar',
                            'precio_preventa', 'porcentaje_descuento', 'es_cortesia' y 'tipo_boleta'.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    if objeto_boleta["tipo_boleta"] == "Bar":
        col_izq.write(f'ID de la Boleta: {objeto_boleta["id_boleta"]}')
        col_der.write(f'Medio de Pago: {objeto_boleta["medio_pago"]}')
        col_izq.write(f'Precio Estandar: {objeto_boleta["precio_estandar"]}')
        col_der.write(f'Precio Preventa: {objeto_boleta["precio_preventa"]}')
        col_izq.write(f'Porcentaje Descuento: {objeto_boleta["porcentaje_descuento"]}')
        col_der.write(f'Es Cortesia: {objeto_boleta["es_cortesia"]}')
        col_izq.write(f'Tipo de Boleta: {objeto_boleta["tipo_boleta"]}')
    elif objeto_boleta["tipo_boleta"] == "Teatro":
        col_izq.write(f'ID de la Boleta: {objeto_boleta["id_boleta"]}')
        col_der.write(f'Medio de Pago: {objeto_boleta["medio_pago"]}')
        col_izq.write(f'Precio Estandar: {objeto_boleta["precio_estandar"]}')
        col_der.write(f'Precio Preventa: {objeto_boleta["precio_preventa"]}')
        col_izq.write(f'Porcentaje Descuento: {objeto_boleta["porcentaje_descuento"]}')
        col_der.write(f'Es Cortesia: {objeto_boleta["es_cortesia"]}')
        col_izq.write(f'Tipo de Boleta: {objeto_boleta["tipo_boleta"]}')
    elif objeto_boleta["tipo_boleta"] == "Filantropico":
        col_izq.write(f'ID de la Boleta: {objeto_boleta["id_boleta"]}')
        col_der.write(f'Medio de Pago: {objeto_boleta["medio_pago"]}')
        col_izq.write(f'Precio Estandar: {objeto_boleta["precio_estandar"]}')
        col_der.write(f'Precio Preventa: {objeto_boleta["precio_preventa"]}')
        col_izq.write(f'Porcentaje Descuento: {objeto_boleta["porcentaje_descuento"]}')
        col_der.write(f'Es Cortesia: {objeto_boleta["es_cortesia"]}')
        col_izq.write(f'Tipo de Boleta: {objeto_boleta["tipo_boleta"]}')


def mostrar_informacion_artista(objeto_artista):
    """
    Función para mostrar información de un artista en la interfaz de usuario.

    Parameters:
    - objeto_artista (dict): Un diccionario que contiene la información del artista
                             con claves 'nombre', 'id_artista' y 'cobro'.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    col_izq.write(f'Nombre del Artista: {objeto_artista["nombre"]}')
    col_der.write(f'ID del Artista: {objeto_artista["id_artista"]}')
    col_izq.write(f'Cobro: {objeto_artista["cobro"]}')


def mostrar_informacion_patrocinador(objeto_patrociador):
    """
    Función para mostrar información de un patrocinador en la interfaz de usuario.

    Parameters:
    - objeto_patrocinador (dict): Un diccionario que contiene la información del patrocinador
                                  con claves 'nombre', 'id_patrocinador' y 'apoyo'.

    Returns:
    - None
    """
    col_izq, col_der = st.columns(2)
    col_izq.write(f'Nombre del Patrocinador: {objeto_patrociador["nombre"]}')
    col_der.write(f'ID del Patrocinador: {objeto_patrociador["id_patrocinador"]}')
    col_izq.write(f'Apoyo Económico: {objeto_patrociador["apoyo"]}')