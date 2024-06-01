

class Artista:
    """
    Clase que representa a un artista.

    Attributes:
    - id_artista (str): El ID del artista.
    - nombre (str): El nombre del artista.
    - cobro (float): El cobro del artista por su participación en un evento.
    """
    def __init__(self, id_artista, nombre, cobro):
        """
        Inicializa un objeto de la clase Artista.

        Parameters:
        - id_artista (str): El ID del artista.
        - nombre (str): El nombre del artista.
        - cobro (float): El cobro del artista por su participación en un evento.
        """
        self.nombre = nombre
        self.id_artista = id_artista
        self.cobro = cobro
