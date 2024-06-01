import unittest
from models.artista import Artista

class TestArtista(unittest.TestCase):

    def test_artista_constructor(self):
        artista = Artista(1, "Artista Test", 500)
        self.assertEqual(artista.id_artista, 1)
        self.assertEqual(artista.nombre, "Artista Test")
        self.assertEqual(artista.cobro, 500)

if __name__ == '__main__':
    unittest.main()