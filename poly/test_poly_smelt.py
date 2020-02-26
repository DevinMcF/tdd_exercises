from unittest import TestCase
from poly_smelt import Polynomial

class TestApp(TestCase):
    def setUp(self):
        self.p1 = Polynomial()

    def empty_polynomial(self):
        """
        Tests the output of an empty instance of Polynomial
        """

        self.assertEqual(str(self.p1),'0')
