import unittest
from models.boleta_bar import BoletaBar

class TestBoletaBar(unittest.TestCase):

    def test_boleta_bar_constructor(self):
        boleta_bar = BoletaBar(1, "Efectivo", 50, 40, 10, False)
        self.assertEqual(boleta_bar.id_boleta, 1)
        self.assertEqual(boleta_bar.medio_pago, "Efectivo")
        self.assertEqual(boleta_bar.precio_estandar, 50)
        self.assertEqual(boleta_bar.precio_preventa, 40)
        self.assertEqual(boleta_bar.porcentaje_descuento, 10)
        self.assertFalse(boleta_bar.es_cortesia)
        self.assertEqual(boleta_bar.porcentaje_ganancias_boleteria, 0)
        self.assertEqual(boleta_bar.tipo_boleta, "Bar")

if __name__ == '__main__':
    unittest.main()