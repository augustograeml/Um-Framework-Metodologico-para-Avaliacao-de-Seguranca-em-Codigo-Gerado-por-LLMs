# Python Application for Dynamic Library Loading

## Overview
This project is a Python application designed to dynamically load user-provided libraries, allowing for extensible functionality. It serves as a framework for users to enhance the application by adding their own modules.

## Project Structure
```
python-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── loader
│   │   ├── __init__.py
│   │   └── dynamic_loader.py
│   └── extensions
│       ├── __init__.py
│       └── sample_extension.py
├── tests
│   ├── __init__.py
│   └── test_dynamic_loader.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd python-app
pip install -r requirements.txt
```

## Usage
To run the application, execute the `main.py` file:

```bash
python app/main.py
```

## Dynamic Loading
The application includes a `DynamicLoader` class located in `app/loader/dynamic_loader.py`. This class provides the following methods:

- `load_library(library_path)`: Dynamically loads a user-provided library from the specified path.
- `unload_library(library_name)`: Unloads the specified library from the application.

## Extensions
Users can create their own extensions by defining functions in the `app/extensions` directory. An example extension is provided in `sample_extension.py`.

## Testing
Unit tests for the `DynamicLoader` class can be found in `tests/test_dynamic_loader.py`. To run the tests, use:

```bash
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.