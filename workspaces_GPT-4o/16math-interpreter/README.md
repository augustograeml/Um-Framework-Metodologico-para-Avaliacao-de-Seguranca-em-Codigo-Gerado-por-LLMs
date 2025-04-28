# Math Interpreter

This project is a Python application that provides an interpreter for mathematical expressions. Users can input calculations in string format and obtain the evaluated result.

## Features

- Interpret mathematical expressions in string format.
- Tokenize expressions for accurate evaluation.
- Evaluate expressions to return numerical results.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd math-interpreter
pip install -r requirements.txt
```

## Usage

To use the interpreter, you can create an instance of the `Interpreter` class and call the `interpret` method with a string expression:

```python
from src.interpreter import Interpreter

interpreter = Interpreter()
result = interpreter.interpret("3 + 5 * (2 - 8)")
print(result)  # Output will be the evaluated result
```

## Running Tests

To ensure everything is working correctly, you can run the unit tests provided in the `tests` directory:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.