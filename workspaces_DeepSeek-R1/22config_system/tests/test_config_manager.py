import unittest
from src.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):

    def setUp(self):
        self.config_manager = ConfigManager()

    def test_load_config(self):
        config = self.config_manager.load_config('configs/saved_configs/config1.json')
        self.assertIsNotNone(config)
        self.assertIn('some_key', config)  # Replace 'some_key' with an actual key from your config

    def test_save_config(self):
        config_data = {'some_key': 'some_value'}  # Replace with actual test data
        self.config_manager.save_config('configs/saved_configs/test_config.json', config_data)
        loaded_config = self.config_manager.load_config('configs/saved_configs/test_config.json')
        self.assertEqual(loaded_config, config_data)

if __name__ == '__main__':
    unittest.main()