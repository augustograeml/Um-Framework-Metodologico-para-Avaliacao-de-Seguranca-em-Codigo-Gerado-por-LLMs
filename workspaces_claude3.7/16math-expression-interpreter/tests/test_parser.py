import unittest
from src.interpreter.lexer import Lexer
from src.interpreter.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def test_simple_expression(self):
        tokens = self.lexer.tokenize("3 + 5")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, ('+', 3, 5))

    def test_nested_expression(self):
        tokens = self.lexer.tokenize("(1 + 2) * 3")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, ('*', ('+', 1, 2), 3))

    def test_expression_with_precedence(self):
        tokens = self.lexer.tokenize("2 + 3 * 4")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, ('+', 2, ('*', 3, 4)))

    def test_invalid_expression(self):
        tokens = self.lexer.tokenize("3 +")
        with self.assertRaises(Exception):
            self.parser.parse(tokens)

if __name__ == '__main__':
    unittest.main()