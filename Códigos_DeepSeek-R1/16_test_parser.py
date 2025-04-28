import unittest
from math_interpreter.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_simple_expression(self):
        tokens = self.parser.tokenize("3 + 5")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, expected_ast)  # Replace expected_ast with the actual expected AST

    def test_parentheses(self):
        tokens = self.parser.tokenize("(1 + 2) * 3")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, expected_ast)  # Replace expected_ast with the actual expected AST

    def test_nested_expressions(self):
        tokens = self.parser.tokenize("2 * (3 + (4 - 1))")
        ast = self.parser.parse(tokens)
        self.assertEqual(ast, expected_ast)  # Replace expected_ast with the actual expected AST

    def test_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            tokens = self.parser.tokenize("3 + * 5")
            self.parser.parse(tokens)

if __name__ == '__main__':
    unittest.main()