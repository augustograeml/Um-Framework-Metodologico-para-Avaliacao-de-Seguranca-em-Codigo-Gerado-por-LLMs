import os
import unittest
from src.utils.auth import load_token

class TestAuthUtils(unittest.TestCase):
    def test_load_token(self):
        # Assuming the .env file is set up correctly and contains a line like: GITHUB_TOKEN=your_token_here
        token = load_token()
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 0)

if __name__ == '__main__':
    unittest.main()