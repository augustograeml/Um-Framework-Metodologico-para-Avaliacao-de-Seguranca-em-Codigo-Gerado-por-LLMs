# Division Calculator

This project is a simple command-line application that allows users to divide two numbers. It handles user input, performs the division operation, and manages division by zero errors gracefully.

## Features

- User-friendly input for two numbers.
- Division operation with error handling for division by zero.
- Modular design with separate files for the calculator logic and user interface.

## Getting Started

To run the application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Run the application using:
   ```
   python src/main.py
   ```

## Usage

When prompted, enter two numbers. The application will display the result of the division. If the second number is zero, an error message will be shown.

## Testing

To run the unit tests for the division functionality, navigate to the `tests` directory and run:
```
python -m unittest test_division.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.