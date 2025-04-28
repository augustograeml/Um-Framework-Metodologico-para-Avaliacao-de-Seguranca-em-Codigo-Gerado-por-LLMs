import os
import sys
from core.dynamic_loader import DynamicLoader

def main():
    print("Initializing the Python Dynamic Loading Application...")
    
    loader = DynamicLoader()
    
    # Example of loading a user-provided plugin
    plugin_name = input("Enter the name of the plugin to load: ")
    try:
        loader.load_plugin(plugin_name)
        print(f"Plugin '{plugin_name}' loaded successfully.")
    except Exception as e:
        print(f"Failed to load plugin '{plugin_name}': {e}")

    # Example of unloading a user-provided plugin
    unload_plugin_name = input("Enter the name of the plugin to unload: ")
    try:
        loader.unload_plugin(unload_plugin_name)
        print(f"Plugin '{unload_plugin_name}' unloaded successfully.")
    except Exception as e:
        print(f"Failed to unload plugin '{unload_plugin_name}': {e}")

if __name__ == "__main__":
    main()