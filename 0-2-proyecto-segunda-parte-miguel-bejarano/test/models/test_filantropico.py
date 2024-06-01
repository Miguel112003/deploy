import unittest
from models.filantropico import Filantropico


class TestFilantropico(unittest.TestCase):

    def test_filantropico_constructor(self):
        filantropico = Filantropico(1, "Filantropico Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100)
        self.assertEqual(filantropico.id_evento, 1)
        self.assertEqual(filantropico.nombre, "Filantropico Test")
        self.assertEqual(filantropico.fecha, "01/01/2024")
        self.assertEqual(filantropico.hora_apertura, "18:00")
        self.assertEqual(filantropico.hora_show, "20:00")
        self.assertEqual(filantropico.lugar, "Lugar Test")
        self.assertEqual(filantropico.direccion, "Dirección Test")
        self.assertEqual(filantropico.ciudad, "Ciudad Test")
        self.assertEqual(filantropico.estado, "Estado Test")
        self.assertEqual(filantropico.aforo_max, 100)
        self.assertEqual(filantropico.aforo_vendido, 0)
        self.assertEqual(filantropico.artistas, {})
        self.assertEqual(filantropico.boletas, {})
        self.assertEqual(filantropico.tipo, "Filantropico")
        self.assertEqual(filantropico.patrocinadores, {})

    def test_aumentar_vendidos(self):
        filantropico = Filantropico(1, "Filantropico Test", "01/01/2024", "18:00", "20:00", "Lugar Test", "Dirección Test", "Ciudad Test", "Estado Test", 100)
        self.assertEqual(filantropico.aforo_vendido, 0)
        filantropico.aumentar_vendidos()
        self.assertEqual(filantropico.aforo_vendido, 1)
        # Verifica que el error sea lanzado si se excede el aforo máximo
        with self.assertRaises(ValueError):
            for _ in range(100):
                filantropico.aumentar_vendidos()

if __name__ == '__main__':
    unittest.main()