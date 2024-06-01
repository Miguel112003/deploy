from models.evento import Evento


class Bar(Evento):
    """
    Clase que representa un evento de tipo Bar.

    """
    def __init__(self, id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                 direccion, estado, ciudad, aforo_maximo, porcentaje_ganancias):
        """
        Inicializa un objeto de la clase Bar.

        Parameters:
        - id_evento (str): El ID del evento.
        - nombre (str): El nombre del evento.
        - fecha (str): La fecha del evento.
        - hora_apertura (str): La hora de apertura del evento.
        - hora_show (str): La hora de inicio del show del evento.
        - lugar (str): El lugar del evento.
        - direccion (str): La dirección del evento.
        - estado (str): El estado del evento.
        - ciudad (str): La ciudad del evento.
        - aforo_maximo (int): El aforo máximo del evento.
        - porcentaje_ganancias (float): El porcentaje de ganancias del bar en el evento.
        """
        super().__init__(id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                         direccion, estado, ciudad, aforo_maximo)
        self.tipo = "Bar"
        self.porcentaje_ganancias_bar = porcentaje_ganancias
        self.porcentaje_ganancias_boleteria = 100 - porcentaje_ganancias

    def aumentar_vendidos(self):
        """
        Aumenta el contador de boletas vendidas para el evento.

        Raises:
        - ValueError: Si se intenta aumentar el contador de boletas vendidas más allá del aforo máximo.
        """
        if self.aforo_vendido < self.aforo_max:
            self.aforo_vendido += 1
        else:
            raise ValueError("El Aforo maximo fue alcanzado")
