import unittest
from models.bar import Bar

class TestBar(unittest.TestCase):

    def test_bar_constructor(self):
        bar = Bar(1, "Bar Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100, 20)
        self.assertEqual(bar.id_evento, 1)
        self.assertEqual(bar.nombre, "Bar Test")
        self.assertEqual(bar.fecha, "01/01/2024")
        self.assertEqual(bar.hora_apertura, "18:00")
        self.assertEqual(bar.hora_show, "20:00")
        self.assertEqual(bar.lugar, "Lugar Test")
        self.assertEqual(bar.direccion, "Dirección Test")
        self.assertEqual(bar.ciudad, "Ciudad Test")
        self.assertEqual(bar.estado, "Estado Test")
        self.assertEqual(bar.aforo_max, 100)
        self.assertEqual(bar.aforo_vendido, 0)
        self.assertEqual(bar.artistas, {})
        self.assertEqual(bar.boletas, {})
        self.assertEqual(bar.tipo, "Bar")
        self.assertEqual(bar.porcentaje_ganancias_bar, 20)
        self.assertEqual(bar.porcentaje_ganancias_boleteria, 80)

    def test_aumentar_vendidos(self):
        bar = Bar(1, "Bar Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100, 20)
        self.assertEqual(bar.aforo_vendido, 0)
        bar.aumentar_vendidos()
        self.assertEqual(bar.aforo_vendido, 1)
        # Verifica que el error sea lanzado si se excede el aforo máximo
        with self.assertRaises(ValueError):
            for _ in range(100):
                bar.aumentar_vendidos()

if __name__ == '__main__':
    unittest.main()