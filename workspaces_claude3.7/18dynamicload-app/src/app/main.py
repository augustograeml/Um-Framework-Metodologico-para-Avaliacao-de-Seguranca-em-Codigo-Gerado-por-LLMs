from plugin_system.loader import PluginLoader
from plugin_system.registry import PluginRegistry
from app.config import CONFIG

def main():
    registry = PluginRegistry()
    loader = PluginLoader(registry)

    # Load plugins from the specified directory
    loader.load_plugins(CONFIG['plugin_directory'])

    # Start the main application event loop
    print("Application started. Loaded plugins:")
    for plugin in registry.get_plugins():
        print(f"- {plugin.name}")

if __name__ == "__main__":
    main()