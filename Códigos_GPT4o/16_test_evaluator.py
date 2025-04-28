import unittest
from src.evaluator import Evaluator

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.evaluator = Evaluator()

    def test_simple_addition(self):
        tokens = ['2', '+', '3']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 5)

    def test_simple_subtraction(self):
        tokens = ['5', '-', '2']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 3)

    def test_simple_multiplication(self):
        tokens = ['4', '*', '2']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 8)

    def test_simple_division(self):
        tokens = ['8', '/', '2']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 4)

    def test_combined_operations(self):
        tokens = ['3', '+', '5', '*', '2']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 13)

    def test_parentheses(self):
        tokens = ['(', '1', '+', '2', ')', '*', '3']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, 9)

    def test_negative_numbers(self):
        tokens = ['-3', '+', '2']
        result = self.evaluator.evaluate(tokens)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()