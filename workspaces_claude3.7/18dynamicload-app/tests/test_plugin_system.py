import unittest
from src.plugin_system.loader import PluginLoader
from src.plugin_system.registry import PluginRegistry

class TestPluginSystem(unittest.TestCase):

    def setUp(self):
        self.plugin_loader = PluginLoader()
        self.plugin_registry = PluginRegistry()

    def test_load_plugin(self):
        plugin_name = 'example_plugin'
        self.plugin_loader.load_plugin(plugin_name)
        self.assertIn(plugin_name, self.plugin_registry.get_plugins())

    def test_load_non_existent_plugin(self):
        with self.assertRaises(Exception):
            self.plugin_loader.load_plugin('non_existent_plugin')

    def test_plugin_interface_implementation(self):
        plugin_name = 'example_plugin'
        self.plugin_loader.load_plugin(plugin_name)
        plugin = self.plugin_registry.get_plugin(plugin_name)
        self.assertTrue(hasattr(plugin, 'run'))
        self.assertTrue(callable(plugin.run))

if __name__ == '__main__':
    unittest.main()