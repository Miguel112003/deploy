from abc import ABC


class Boleta(ABC):
    def __init__(self, id_boleta, medio_pago, precio_estandar, precio_preventa, porcentaje_descuento,
                 es_cortesia):
        """
        Clase abstracta que representa una boleta.

        Attributes:
        - id_boleta (str): El ID de la boleta.
        - medio_pago (str): El medio de pago utilizado para la compra de la boleta.
        - medio_enterado (str): El medio por el cual el usuario se enteró del evento.
        - precio_estandar (float): El precio estándar de la boleta.
        - precio_preventa (float): El precio de preventa de la boleta.
        - porcentaje_descuento (float): El porcentaje de descuento aplicado a la boleta.
        - es_cortesia (str): Indica si la boleta es cortesía o no.
        - nombre_usuario (str): El nombre del usuario que compró la boleta.
        - documento_usuario (str): El documento del usuario que compró la boleta.
        - correo_usuario (str): El correo electrónico del usuario que compró la boleta.
        - vendida (bool): Indica si la boleta ha sido vendida o no.
        - tipo_venta (str): El tipo de venta de la boleta.
        """
        self.id_boleta = id_boleta
        self.medio_pago = medio_pago
        self.medio_enterado = ""
        self.precio_estandar = precio_estandar
        self.precio_preventa = precio_preventa
        self.porcentaje_descuento = porcentaje_descuento
        self.es_cortesia = es_cortesia
        self.nombre_usuario = ""
        self.documento_usuario = ""
        self.correo_usuario = ""
        self.vendida = False
        self.tipo_venta = ''
