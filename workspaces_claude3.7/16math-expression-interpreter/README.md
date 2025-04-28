# Math Expression Interpreter

This project is a Python application that allows users to input mathematical expressions in string format and obtain the calculated results. The application consists of several components that work together to tokenize, parse, and evaluate mathematical expressions.

## Features

- Tokenization of input strings to identify numbers, operators, and parentheses.
- Parsing of tokens to construct an abstract syntax tree (AST).
- Evaluation of the AST to compute the final result of the expression.

## Project Structure

```
math-expression-interpreter
├── src
│   ├── __init__.py
│   ├── interpreter
│   │   ├── __init__.py
│   │   ├── lexer.py
│   │   ├── parser.py
│   │   └── evaluator.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_evaluator.py
├── examples
│   └── basic_usage.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To use the interpreter, run the `main.py` file:

```
python src/main.py
```

You will be prompted to enter a mathematical expression. The interpreter will then output the result of the calculation.

## Example

For a quick example, you can check the `examples/basic_usage.py` file, which demonstrates how to use the interpreter programmatically.

## Testing

To run the unit tests for the application, navigate to the `tests` directory and run:

```
pytest
```

This will execute all the tests defined in the `test_lexer.py`, `test_parser.py`, and `test_evaluator.py` files.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.