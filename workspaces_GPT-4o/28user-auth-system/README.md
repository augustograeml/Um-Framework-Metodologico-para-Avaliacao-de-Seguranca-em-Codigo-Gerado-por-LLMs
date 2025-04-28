# User Authentication System

This project is a user authentication system built with Python and Flask. It provides functionalities for user registration, login, and password management.

## Project Structure

```
user-auth-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── database
│   │   ├── __init__.py
│   │   └── connection.py
│   └── tests
│       ├── __init__.py
│       └── test_auth.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd user-auth-system
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app/main.py
   ```
2. Access the API endpoints for user registration and login.

## Testing

To run the tests for the authentication system, navigate to the `app/tests` directory and run:
```
pytest test_auth.py
```

## License

This project is licensed under the MIT License.