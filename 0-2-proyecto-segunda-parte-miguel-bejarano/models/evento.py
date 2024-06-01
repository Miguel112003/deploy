from abc import ABC, abstractmethod


class Evento(ABC):
    """
    Clase abstracta que representa un evento.

    Methods:
    - aumentar_vendidos(): Método abstracto para aumentar el número de boletas vendidas del evento.
    """
    def __init__(self, id_evento, nombre, fecha, hora_apertura, hora_show,
                 lugar, direccion, ciudad, estado, aforo_maximo):
        """
        Inicializa un objeto de la clase Evento.

        Parameters:
        - id_evento (str): El ID único del evento.
        - nombre (str): El nombre del evento.
        - fecha (str): La fecha del evento.
        - hora_apertura (str): La hora de apertura del evento.
        - hora_show (str): La hora de inicio del show del evento.
        - lugar (str): El lugar donde se realizará el evento.
        - direccion (str): La dirección del lugar del evento.
        - ciudad (str): La ciudad donde se llevará a cabo el evento.
        - estado (str): El estado actual del evento.
        - aforo_maximo (int): El aforo máximo permitido para el evento.
        """
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = fecha
        self.hora_apertura = hora_apertura
        self.hora_show = hora_show
        self.lugar = lugar
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.artistas = {}
        self.aforo_max = aforo_maximo
        self.aforo_vendido = 0
        self.boletas = {}

    @abstractmethod
    def aumentar_vendidos(self):
        """
        Método abstracto para aumentar el número de boletas vendidas del evento.
        """
        pass
