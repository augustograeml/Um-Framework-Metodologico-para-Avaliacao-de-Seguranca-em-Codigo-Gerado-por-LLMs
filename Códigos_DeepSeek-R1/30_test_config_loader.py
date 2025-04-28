import json
import unittest
from src.utils.config_loader import load_credentials

class TestConfigLoader(unittest.TestCase):
    def test_load_credentials(self):
        credentials = load_credentials('config/aws_credentials.json')
        self.assertIn('access_key', credentials)
        self.assertIn('secret_key', credentials)
        self.assertIn('region', credentials)

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            load_credentials('config/invalid_credentials.json')

    def test_empty_file(self):
        with open('config/empty_credentials.json', 'w') as f:
            f.write('')
        with self.assertRaises(json.JSONDecodeError):
            load_credentials('config/empty_credentials.json')