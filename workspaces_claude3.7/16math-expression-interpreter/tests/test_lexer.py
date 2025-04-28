import unittest
from src.interpreter.lexer import Lexer

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()

    def test_tokenize_simple_expression(self):
        expression = "3 + 5"
        expected_tokens = [('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '5')]
        self.assertEqual(self.lexer.tokenize(expression), expected_tokens)

    def test_tokenize_expression_with_parentheses(self):
        expression = "(1 + 2) * 3"
        expected_tokens = [('LPAREN', '('), ('NUMBER', '1'), ('PLUS', '+'), ('NUMBER', '2'), ('RPAREN', ')'), ('MULTIPLY', '*'), ('NUMBER', '3')]
        self.assertEqual(self.lexer.tokenize(expression), expected_tokens)

    def test_tokenize_expression_with_negative_numbers(self):
        expression = "-4 + 2"
        expected_tokens = [('MINUS', '-'), ('NUMBER', '4'), ('PLUS', '+'), ('NUMBER', '2')]
        self.assertEqual(self.lexer.tokenize(expression), expected_tokens)

    def test_tokenize_invalid_expression(self):
        expression = "3 + * 5"
        with self.assertRaises(ValueError):
            self.lexer.tokenize(expression)

if __name__ == '__main__':
    unittest.main()