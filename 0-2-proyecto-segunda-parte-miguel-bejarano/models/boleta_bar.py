from models.boleta import Boleta


class BoletaBar(Boleta):
    """
    Clase que representa una boleta para un evento de tipo bar.

    Attributes:
    - porcentaje_ganancias_boleteria (float): El porcentaje de ganancias de la boletería para el evento de tipo bar.
    - tipo_boleta (str): El tipo de boleta, que en este caso es "Bar".
    """
    def __init__(self, id_boleta, medio_pago, precio_estandar, precio_preventa, porcentaje_descuento, es_cortesia):
        """
        Inicializa un objeto de la clase BoletaBar.

        Parameters:
        - id_boleta (str): El ID de la boleta.
        - medio_pago (str): El medio de pago utilizado para la compra de la boleta.
        - precio_estandar (float): El precio estándar de la boleta.
        - precio_preventa (float): El precio de preventa de la boleta.
        - porcentaje_descuento (float): El porcentaje de descuento aplicado a la boleta.
        - es_cortesia (str): Indica si la boleta es cortesía o no.
        """
        super().__init__(id_boleta, medio_pago, precio_estandar, precio_preventa, porcentaje_descuento, es_cortesia)
        self.porcentaje_ganancias_boleteria = 0
        self.tipo_boleta = "Bar"
