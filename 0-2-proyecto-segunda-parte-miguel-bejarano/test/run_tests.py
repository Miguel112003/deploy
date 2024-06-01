import unittest

if __name__ == '__main__':
    # Descubre y carga todos los tests desde los subdirectorios "controller" y "models"
    test_suite = unittest.TestLoader().discover('controller', pattern='test_*.py')
    test_suite.addTests(unittest.TestLoader().discover('models', pattern='test_*.py'))
    # Ejecuta los tests y muestra los resultados en la consola
    unittest.TextTestRunner(verbosity=2).run(test_suite)