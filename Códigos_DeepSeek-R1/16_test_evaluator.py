import unittest
from math_interpreter.evaluator import Evaluator
from math_interpreter.parser import Parser
from math_interpreter.lexer import Lexer

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.evaluator = Evaluator()

    def test_evaluate_addition(self):
        expression = "3 + 5"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 8)

    def test_evaluate_subtraction(self):
        expression = "10 - 4"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 6)

    def test_evaluate_multiplication(self):
        expression = "7 * 6"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 42)

    def test_evaluate_division(self):
        expression = "20 / 4"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 5)

    def test_evaluate_complex_expression(self):
        expression = "3 + 5 * 2 - 8 / 4"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()