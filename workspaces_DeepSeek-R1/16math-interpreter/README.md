# Math Interpreter

This project is a Python application that implements an interpreter for mathematical expressions. Users can input calculations in string format, and the interpreter will return the computed result.

## Features

- Tokenization of mathematical expressions
- Parsing of tokens to construct an Abstract Syntax Tree (AST)
- Evaluation of the AST to compute results
- User-friendly command-line interface

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the math interpreter, run the following command:

```
python src/main.py
```

You will be prompted to enter a mathematical expression. After inputting your expression, the interpreter will output the result.

## Running Tests

To run the unit tests for the project, execute:

```
pytest
```

This will run all tests located in the `tests` directory.

## Project Structure

```
math-interpreter
├── src
│   ├── math_interpreter
│   │   ├── __init__.py
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   └── evaluator.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_evaluator.py
├── README.md
├── requirements.txt
└── setup.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.