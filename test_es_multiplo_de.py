import unittest

from es_multiplo_de import es_multiplo_de


class TestEsMultiploDe(unittest.TestCase):

    def test_multiplo_exacto_devuelve_true(self):
        self.assertTrue(es_multiplo_de(10, 5))

    def test_no_multiplo_devuelve_false(self):
        self.assertFalse(es_multiplo_de(10, 3))

    def test_cero_es_multiplo_de_cualquier_numero(self):
        self.assertTrue(es_multiplo_de(0, 7))

    def test_m_igual_a_cero_devuelve_false(self):
        self.assertFalse(es_multiplo_de(10, 0))

    def test_n_negativo_multiplo_de_m_positivo(self):
        self.assertTrue(es_multiplo_de(-10, 5))

    def test_n_positivo_multiplo_de_m_negativo(self):
        self.assertTrue(es_multiplo_de(10, -5))

    def test_ambos_negativos_multiplo(self):
        self.assertTrue(es_multiplo_de(-10, -5))

    def test_negativo_no_multiplo_devuelve_false(self):
        self.assertFalse(es_multiplo_de(-10, 3))


if __name__ == "__main__":
    unittest.main()
