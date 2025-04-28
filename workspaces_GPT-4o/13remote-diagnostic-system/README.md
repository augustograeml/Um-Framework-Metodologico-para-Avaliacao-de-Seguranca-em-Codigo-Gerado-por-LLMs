# Remote Diagnostic System

This project is a remote diagnostic system built with Python. It allows users to execute operating system commands through a web interface, providing a convenient way to perform diagnostics and retrieve command outputs.

## Features

- Execute system commands remotely via a web interface
- Display command output in real-time
- User-friendly HTML interface
- Modular architecture with separate services for command execution

## Project Structure

```
remote-diagnostic-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── commands.py
│   ├── services
│   │   ├── __init__.py
│   │   └── executor.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── styles.css
├── tests
│   ├── __init__.py
│   ├── test_commands.py
│   └── test_executor.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd remote-diagnostic-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python app/main.py
```

## Testing

To run the tests, use:
```
pytest
```

## Environment Variables

Create a `.env` file in the root directory and define any necessary environment variables as specified in `.env.example`.

## License

This project is licensed under the MIT License.