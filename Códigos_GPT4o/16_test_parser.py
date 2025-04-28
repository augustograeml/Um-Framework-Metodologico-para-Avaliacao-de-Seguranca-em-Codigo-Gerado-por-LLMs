import unittest
from src.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_simple_expression(self):
        expression = "3 + 5"
        expected_tokens = ["3", "+", "5"]
        self.assertEqual(self.parser.parse(expression), expected_tokens)

    def test_expression_with_parentheses(self):
        expression = "(1 + 2) * 3"
        expected_tokens = ["(", "1", "+", "2", ")", "*", "3"]
        self.assertEqual(self.parser.parse(expression), expected_tokens)

    def test_expression_with_multiple_operations(self):
        expression = "4 * 5 - 6 / 2"
        expected_tokens = ["4", "*", "5", "-", "6", "/", "2"]
        self.assertEqual(self.parser.parse(expression), expected_tokens)

    def test_expression_with_whitespace(self):
        expression = "  7   +  8  "
        expected_tokens = ["7", "+", "8"]
        self.assertEqual(self.parser.parse(expression), expected_tokens)

    def test_invalid_expression(self):
        expression = "3 + * 5"
        with self.assertRaises(ValueError):
            self.parser.parse(expression)

if __name__ == '__main__':
    unittest.main()