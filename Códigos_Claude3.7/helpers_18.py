def load_plugin(plugin_path):
    import importlib.util
    import os

    if not os.path.isfile(plugin_path):
        raise FileNotFoundError(f"Plugin file not found: {plugin_path}")

    plugin_name = os.path.splitext(os.path.basename(plugin_path))[0]
    spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
    plugin_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(plugin_module)

    return plugin_module

def list_plugins(plugins_directory):
    import os

    if not os.path.isdir(plugins_directory):
        raise NotADirectoryError(f"Plugins directory not found: {plugins_directory}")

    return [f for f in os.listdir(plugins_directory) if f.endswith('.py') and f != '__init__.py']