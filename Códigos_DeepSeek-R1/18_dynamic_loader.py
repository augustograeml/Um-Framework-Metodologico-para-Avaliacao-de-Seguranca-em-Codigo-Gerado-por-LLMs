class DynamicLoader:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin_name):
        try:
            module = __import__(f'plugins.{plugin_name}', fromlist=[''])
            self.plugins[plugin_name] = module
            return module
        except ImportError as e:
            print(f"Error loading plugin '{plugin_name}': {e}")
            return None

    def unload_plugin(self, plugin_name):
        if plugin_name in self.plugins:
            del self.plugins[plugin_name]
            print(f"Plugin '{plugin_name}' unloaded.")
        else:
            print(f"Plugin '{plugin_name}' not loaded.")