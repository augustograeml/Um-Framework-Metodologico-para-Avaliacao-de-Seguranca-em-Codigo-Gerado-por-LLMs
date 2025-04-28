import unittest
from src.calculator.division import divide

class TestDivision(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_positive_negative(self):
        self.assertEqual(divide(10, -2), -5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()