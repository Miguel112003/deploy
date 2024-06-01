

class Patrocinador:
    """
    Clase que representa a un patrocinador de un evento.

    Attributes:
    - id_patrocinador (str): El ID único del patrocinador.
    - nombre (str): El nombre del patrocinador.
    - apoyo (float): El apoyo económico brindado por el patrocinador.

    Methods:
    - __init__(id_patrocinador, nombre, apoyo): Constructor de la clase.
    """

    def __init__(self, id_patrocinador, nombre, apoyo):
        """
        Inicializa un objeto de la clase Patrocinador.

        Parameters:
        - id_patrocinador (str): El ID único del patrocinador.
        - nombre (str): El nombre del patrocinador.
        - apoyo (float): El apoyo económico brindado por el patrocinador.
        """
        self.id_patrocinador = id_patrocinador
        self.nombre = nombre
        self.apoyo = apoyo
