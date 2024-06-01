import unittest
from models.patrocinador import Patrocinador

class TestPatrocinador(unittest.TestCase):

    def test_patrocinador_constructor(self):
        patrocinador = Patrocinador(1, "Patrocinador Test", 1000)
        self.assertEqual(patrocinador.id_patrocinador, 1)
        self.assertEqual(patrocinador.nombre, "Patrocinador Test")
        self.assertEqual(patrocinador.apoyo, 1000)

if __name__ == '__main__':
    unittest.main()