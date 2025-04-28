import unittest
from math_interpreter.lexer import Lexer

class TestLexer(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()

    def test_tokenize_single_number(self):
        result = self.lexer.tokenize("42")
        self.assertEqual(result, [('NUMBER', '42')])

    def test_tokenize_addition(self):
        result = self.lexer.tokenize("3 + 5")
        self.assertEqual(result, [('NUMBER', '3'), ('PLUS', '+'), ('NUMBER', '5')])

    def test_tokenize_subtraction(self):
        result = self.lexer.tokenize("10 - 2")
        self.assertEqual(result, [('NUMBER', '10'), ('MINUS', '-'), ('NUMBER', '2')])

    def test_tokenize_multiplication(self):
        result = self.lexer.tokenize("4 * 5")
        self.assertEqual(result, [('NUMBER', '4'), ('MULTIPLY', '*'), ('NUMBER', '5')])

    def test_tokenize_division(self):
        result = self.lexer.tokenize("20 / 4")
        self.assertEqual(result, [('NUMBER', '20'), ('DIVIDE', '/'), ('NUMBER', '4')])

    def test_tokenize_complex_expression(self):
        result = self.lexer.tokenize("3 + 5 * 2 - 8 / 4")
        self.assertEqual(result, [
            ('NUMBER', '3'), 
            ('PLUS', '+'), 
            ('NUMBER', '5'), 
            ('MULTIPLY', '*'), 
            ('NUMBER', '2'), 
            ('MINUS', '-'), 
            ('NUMBER', '8'), 
            ('DIVIDE', '/'), 
            ('NUMBER', '4')
        ])

if __name__ == '__main__':
    unittest.main()