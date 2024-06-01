from models.evento import Evento


class Teatro(Evento):
    """
    Clase que representa un evento de tipo Teatro.

    Methods:
    - __init__(id_evento, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado,
                                                                    aforo_maximo, alquiler_teatro):
        Constructor de la clase.
    - aumentar_vendidos(): Incrementa el contador de boletas vendidas para el evento.
    """
    def __init__(self, id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                 direccion, ciudad, estado, aforo_maximo, alquiler_teatro):
        """
        Inicializa un objeto de la clase Teatro.

        Parameters:
        - id_evento (str): El ID único del evento.
        - nombre (str): El nombre del evento.
        - fecha (str): La fecha del evento en formato DD/MM/AAAA.
        - hora_apertura (str): La hora de apertura del evento en formato HH:MM.
        - hora_show (str): La hora de inicio del espectáculo en formato HH:MM.
        - lugar (str): El lugar donde se realizará el evento.
        - direccion (str): La dirección del lugar donde se realizará el evento.
        - ciudad (str): La ciudad donde se realizará el evento.
        - estado (str): El estado actual del evento.
        - aforo_maximo (int): El aforo máximo permitido para el evento.
        - alquiler_teatro (float): El costo del alquiler del teatro para el evento.
        """
        super().__init__(id_evento, nombre, fecha, hora_apertura, hora_show, lugar,
                         direccion, ciudad, estado, aforo_maximo)
        self.tipo = "Teatro"
        self.alquiler = alquiler_teatro

    def aumentar_vendidos(self):
        """
        Incrementa el contador de boletas vendidas para el evento.
        """
        if self.aforo_vendido < self.aforo_max:
            self.aforo_vendido += 1
        else:
            raise ValueError("El Aforo maximo fue alcanzado")
