import unittest
from models.boleta_teatro import BoletaTeatro

class TestBoletaTeatro(unittest.TestCase):

    def test_boleta_teatro_constructor(self):
        boleta_teatro = BoletaTeatro(1, "Transferencia", 120, 100, 20, False)
        self.assertEqual(boleta_teatro.id_boleta, 1)
        self.assertEqual(boleta_teatro.medio_pago, "Transferencia")
        self.assertEqual(boleta_teatro.precio_estandar, 120)
        self.assertEqual(boleta_teatro.precio_preventa, 100)
        self.assertEqual(boleta_teatro.porcentaje_descuento, 20)
        self.assertFalse(boleta_teatro.es_cortesia)
        self.assertEqual(boleta_teatro.porencentaje_retencion, 7)
        self.assertEqual(boleta_teatro.tipo_boleta, "Teatro")

if __name__ == '__main__':
    unittest.main()