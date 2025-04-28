class PluginLoader:
    def __init__(self, plugin_directory):
        self.plugin_directory = plugin_directory
        self.plugins = {}

    def load_plugins(self):
        import os
        import importlib.util

        for filename in os.listdir(self.plugin_directory):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = filename[:-3]
                self.load_plugin(plugin_name)

    def load_plugin(self, plugin_name):
        plugin_path = os.path.join(self.plugin_directory, f"{plugin_name}.py")
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        self.plugins[plugin_name] = plugin_module

    def get_plugin(self, plugin_name):
        return self.plugins.get(plugin_name)

    def list_plugins(self):
        return list(self.plugins.keys())