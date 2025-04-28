import unittest
from src.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.interpreter = Interpreter()

    def test_addition(self):
        self.assertEqual(self.interpreter.interpret("2 + 2"), 4)

    def test_subtraction(self):
        self.assertEqual(self.interpreter.interpret("5 - 3"), 2)

    def test_multiplication(self):
        self.assertEqual(self.interpreter.interpret("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(self.interpreter.interpret("10 / 2"), 5)

    def test_combined_operations(self):
        self.assertEqual(self.interpreter.interpret("2 + 3 * 4"), 14)

    def test_parentheses(self):
        self.assertEqual(self.interpreter.interpret("(1 + 2) * 3"), 9)

    def test_negative_numbers(self):
        self.assertEqual(self.interpreter.interpret("-1 + 1"), 0)

    def test_float_numbers(self):
        self.assertEqual(self.interpreter.interpret("2.5 + 2.5"), 5.0)

    def test_invalid_expression(self):
        with self.assertRaises(Exception):
            self.interpreter.interpret("2 + ")

if __name__ == '__main__':
    unittest.main()