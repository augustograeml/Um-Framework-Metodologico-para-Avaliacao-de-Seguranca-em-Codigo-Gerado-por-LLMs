import unittest
from config_system.loader import Loader

class TestLoader(unittest.TestCase):

    def setUp(self):
        self.loader = Loader()

    def test_load_config(self):
        # Test loading a valid configuration file
        config = self.loader.load_config('valid_config.json')
        self.assertIsNotNone(config)
        self.assertIn('key', config)  # Replace 'key' with an expected key in your config

    def test_load_invalid_config(self):
        # Test loading an invalid configuration file
        with self.assertRaises(FileNotFoundError):
            self.loader.load_config('invalid_config.json')

    def test_get_config(self):
        # Test getting the loaded configuration
        self.loader.load_config('valid_config.json')
        config = self.loader.get_config()
        self.assertIsNotNone(config)
        self.assertIn('key', config)  # Replace 'key' with an expected key in your config

if __name__ == '__main__':
    unittest.main()