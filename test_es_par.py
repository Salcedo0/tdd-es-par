import unittest
from math_utils import es_par

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))
    def test_9_es_impar(self):
        self.assertFalse(es_par(9))
    def test_0_es_par(self):
        self.assertTrue(es_par(0))
    def test_negativo_es_par(self):
        self.assertTrue(es_par(-4)) 
        self.assertFalse(es_par(-7))
if __name__ == '__main__':
    unittest.main()