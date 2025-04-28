# Python Dynamic Loading Application

## Overview
This project is a Python application designed to dynamically load user-provided libraries, allowing for extensible functionalities. The application serves as a framework where users can add their own plugins to enhance the system's capabilities.

## Project Structure
```
python-dynamic-loading-app
├── src
│   ├── main.py                # Entry point of the application
│   ├── core
│   │   ├── __init__.py        # Core package initializer
│   │   └── dynamic_loader.py   # Contains the DynamicLoader class for loading plugins
│   └── plugins
│       ├── __init__.py        # Plugins package initializer
│       └── (user-provided libraries go here)  # Place your plugin modules here
├── tests
│   ├── __init__.py            # Tests package initializer
│   ├── test_main.py           # Unit tests for main application logic
│   └── test_dynamic_loader.py  # Unit tests for the DynamicLoader class
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Files and directories to ignore in version control
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-dynamic-loading-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. To run the application, execute:
   ```
   python src/main.py
   ```

2. To add a new plugin, create a new Python file in the `src/plugins` directory. Ensure that the plugin follows the required interface for compatibility.

## Testing
To run the tests, use:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.