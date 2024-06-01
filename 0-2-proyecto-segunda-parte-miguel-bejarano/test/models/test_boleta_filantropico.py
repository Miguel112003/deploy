import unittest
from models.boleta_filantropico import BoletaFilantropico

class TestBoletaFilantropico(unittest.TestCase):

    def test_boleta_filantropico_constructor(self):
        boleta_filantropico = BoletaFilantropico(1, "Tarjeta", 100, 80, 20, True)
        self.assertEqual(boleta_filantropico.id_boleta, 1)
        self.assertEqual(boleta_filantropico.medio_pago, "Tarjeta")
        self.assertEqual(boleta_filantropico.precio_estandar, 100)
        self.assertEqual(boleta_filantropico.precio_preventa, 80)
        self.assertEqual(boleta_filantropico.porcentaje_descuento, 20)
        self.assertTrue(boleta_filantropico.es_cortesia)
        self.assertEqual(boleta_filantropico.tipo_boleta, "Filantropico")

if __name__ == '__main__':
    unittest.main()