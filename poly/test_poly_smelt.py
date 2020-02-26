from unittest import TestCase
from poly_smelt import Polynomial

class TestApp(TestCase):
    def setUp(self):
        self.p1 = Polynomial()

    def test_empty_polynomial(self):
        """
        Tests the output of an empty instance of Polynomial
        """

        self.assertEqual(str(self.p1),'0')

    def test_constant_polynomial(self):
        """
        Tests for a non zero output of a Polynomial with non zero data
        """
        self.p2 = Polynomial('42')
        self.assertEqual(str(self.p2),'42')
