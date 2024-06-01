import unittest
from models.teatro import Teatro

class TestTeatro(unittest.TestCase):

    def test_teatro_constructor(self):
        teatro = Teatro(1, "Teatro Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100, 500)
        self.assertEqual(teatro.id_evento, 1)
        self.assertEqual(teatro.nombre, "Teatro Test")
        self.assertEqual(teatro.fecha, "01/01/2024")
        self.assertEqual(teatro.hora_apertura, "18:00")
        self.assertEqual(teatro.hora_show, "20:00")
        self.assertEqual(teatro.lugar, "Lugar Test")
        self.assertEqual(teatro.direccion, "Dirección Test")
        self.assertEqual(teatro.ciudad, "Ciudad Test")
        self.assertEqual(teatro.estado, "Estado Test")
        self.assertEqual(teatro.aforo_max, 100)
        self.assertEqual(teatro.aforo_vendido, 0)
        self.assertEqual(teatro.artistas, {})
        self.assertEqual(teatro.boletas, {})
        self.assertEqual(teatro.tipo, "Teatro")
        self.assertEqual(teatro.alquiler, 500)

    def test_aumentar_vendidos(self):
        teatro = Teatro(1, "Teatro Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100, 500)
        self.assertEqual(teatro.aforo_vendido, 0)
        teatro.aumentar_vendidos()
        self.assertEqual(teatro.aforo_vendido, 1)
        # Verifica que el error sea lanzado si se excede el aforo máximo
        with self.assertRaises(ValueError):
            for _ in range(100):
                teatro.aumentar_vendidos()

if __name__ == '__main__':
    unittest.main()