# Login System

This project implements a simple login system with a numeric verification code for user authentication. 

## Features

- User login with credentials
- Numeric verification code sent to users
- Logout functionality
- Basic HTML templates for user interaction

## Project Structure

```
login_system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── verification.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── database.py
│   └── templates
│       ├── login.html
│       ├── verify.html
│       └── home.html
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_verification.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd login_system
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
2. Access the application in your web browser at `http://localhost:5000`.

## Testing

To run the tests, use:
```
pytest tests/
```

## License

This project is licensed under the MIT License.