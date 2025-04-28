class PluginRegistry:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        if name in self.plugins:
            raise ValueError(f"Plugin '{name}' is already registered.")
        self.plugins[name] = plugin

    def get_plugin(self, name):
        return self.plugins.get(name)

    def list_plugins(self):
        return list(self.plugins.keys())