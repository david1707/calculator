import unittest

from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(add(5, 6), 11)
        self.assertNotEqual(add(10, 20), 891234903)

    def test_resta(self):
        self.assertEqual(subtract(20, 5), 15)
        self.assertNotEqual(subtract(20, 15), 3)

    def test_multiplicacio(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertNotEqual(multiply(10, 3), 31)

    def test_divisio(self):
        self.assertEqual(divide(15, 3), 5)
        self.assertNotEqual(divide(20, 5), 5)


if __name__ == "__main__":
    unittest.main()
