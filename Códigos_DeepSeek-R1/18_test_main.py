import unittest
from src.core.dynamic_loader import DynamicLoader

class TestMain(unittest.TestCase):
    def setUp(self):
        self.loader = DynamicLoader()

    def test_load_plugin(self):
        # Assuming a plugin named 'example_plugin' exists in the plugins directory
        plugin_name = 'example_plugin'
        self.loader.load_plugin(plugin_name)
        self.assertIn(plugin_name, self.loader.loaded_plugins)

    def test_unload_plugin(self):
        plugin_name = 'example_plugin'
        self.loader.load_plugin(plugin_name)
        self.loader.unload_plugin(plugin_name)
        self.assertNotIn(plugin_name, self.loader.loaded_plugins)

    def test_initialization(self):
        self.assertIsNotNone(self.loader)

if __name__ == '__main__':
    unittest.main()