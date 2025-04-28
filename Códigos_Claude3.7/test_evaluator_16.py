import unittest
from src.interpreter.evaluator import Evaluator
from src.interpreter.parser import Parser
from src.interpreter.lexer import Lexer

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.evaluator = Evaluator()

    def test_evaluate_simple_expression(self):
        expression = "3 + 5"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 8)

    def test_evaluate_complex_expression(self):
        expression = "2 * (3 + 4)"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 14)

    def test_evaluate_expression_with_subtraction(self):
        expression = "10 - 4 + 2"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 8)

    def test_evaluate_expression_with_division(self):
        expression = "8 / 2 + 3"
        tokens = self.lexer.tokenize(expression)
        ast = self.parser.parse(tokens)
        result = self.evaluator.evaluate(ast)
        self.assertEqual(result, 7)

    def test_evaluate_invalid_expression(self):
        expression = "3 +"
        tokens = self.lexer.tokenize(expression)
        with self.assertRaises(Exception):
            ast = self.parser.parse(tokens)
            self.evaluator.evaluate(ast)

if __name__ == '__main__':
    unittest.main()