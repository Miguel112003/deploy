from models.evento import Evento


class Filantropico(Evento):
    """
    Clase que representa un evento filantrópico.

    Methods:
    - aumentar_vendidos(): Aumenta el número de boletas vendidas del evento.
    """
    def __init__(self, id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                 direccion, ciudad, estado, aforo_maximo):
        """
        Clase que representa un evento filantrópico.

        Attributes:
        - id_evento (str): El ID único del evento.
        - nombre (str): El nombre del evento.
        - fecha (str): La fecha del evento.
        - hora_apertura (str): La hora de apertura del evento.
        - hora_show (str): La hora de inicio del show del evento.
        - lugar (str): El lugar donde se realizará el evento.
        - direccion (str): La dirección del lugar del evento.
        - ciudad (str): La ciudad donde se llevará a cabo el evento.
        - estado (str): El estado actual del evento.
        - artistas (dict): Un diccionario que contiene los artistas asociados al evento.
        - aforo_max (int): El aforo máximo permitido para el evento.
        - aforo_vendido (int): El aforo vendido hasta el momento para el evento.
        - boletas (dict): Un diccionario que contiene las boletas asociadas al evento.
        - tipo (str): El tipo de evento, que en este caso es "Filantropico".
        - patrocinadores (dict): Un diccionario que contiene los patrocinadores asociados al evento.

        Methods:
        - aumentar_vendidos(): Aumenta el número de boletas vendidas del evento.
        """
        super().__init__(id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                         direccion, ciudad, estado, aforo_maximo)
        self.tipo = "Filantropico"
        self.patrocinadores = {}

    def aumentar_vendidos(self):
        """
        Aumenta el número de boletas vendidas del evento.
        """
        if self.aforo_vendido < self.aforo_max:
            self.aforo_vendido += 1
        else:
            raise ValueError("El Aforo maximo fue alcanzado")
