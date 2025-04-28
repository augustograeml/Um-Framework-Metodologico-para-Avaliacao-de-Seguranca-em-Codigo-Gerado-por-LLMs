# API Reference for Dynamic Load Application

## Overview

This document provides an overview of the public interfaces available in the Dynamic Load Application. It includes details about the main components, their methods, and usage examples.

## Application Module

### `app`

#### `main.py`

- **Function:** `run()`
  - **Description:** Initializes the application and starts the main event loop.
  - **Usage:**
    ```python
    from app.main import run
    run()
    ```

#### `config.py`

- **Configuration Settings:**
  - `DEFAULT_PLUGIN_PATH`: Default path where plugins are loaded from.
  - `LOG_LEVEL`: Level of logging for the application.

## Plugin System Module

### `plugin_system`

#### `loader.py`

- **Class:** `PluginLoader`
  - **Methods:**
    - `load_plugin(plugin_path: str) -> PluginInterface`
      - **Description:** Loads a plugin from the specified path.
      - **Parameters:** 
        - `plugin_path`: Path to the plugin file.
      - **Returns:** An instance of a class that implements `PluginInterface`.

#### `plugin_interface.py`

- **Class:** `PluginInterface`
  - **Methods:**
    - `execute()`
      - **Description:** Executes the plugin's main functionality.
      - **Returns:** Result of the plugin execution.

#### `registry.py`

- **Class:** `PluginRegistry`
  - **Methods:**
    - `register(plugin: PluginInterface)`
      - **Description:** Registers a loaded plugin.
    - `get_plugins() -> List[PluginInterface]`
      - **Description:** Returns a list of all registered plugins.

## Utility Module

### `utils`

#### `helpers.py`

- **Functions:**
  - `load_json(file_path: str) -> dict`
    - **Description:** Loads a JSON file and returns its contents as a dictionary.

## Example Plugin

### `example_plugin`

#### `plugin.py`

- **Class:** `ExamplePlugin`
  - **Methods:**
    - `execute()`
      - **Description:** An example implementation of the plugin's functionality.

## Usage Example

To load and execute a plugin, you can use the following code:

```python
from plugin_system.loader import PluginLoader
from plugin_system.registry import PluginRegistry

loader = PluginLoader()
registry = PluginRegistry()

plugin = loader.load_plugin('path/to/plugin')
registry.register(plugin)

result = plugin.execute()
print(result)
```

## Conclusion

This API reference provides a high-level overview of the components and their functionalities within the Dynamic Load Application. For more detailed information on plugin development, please refer to the Plugin Development Guide.