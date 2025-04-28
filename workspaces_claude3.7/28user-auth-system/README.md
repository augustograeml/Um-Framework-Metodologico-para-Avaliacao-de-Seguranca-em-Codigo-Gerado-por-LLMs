# User Authentication System

This project is a user authentication system built with Python. It provides functionalities for user registration, login, and secure password management using JWT tokens.

## Features

- User registration and login
- Password hashing and verification
- JWT token creation and verification
- User data validation using Pydantic schemas
- Database management for user data

## Project Structure

```
user-auth-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── jwt.py
│   │   ├── password.py
│   │   └── routes.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── routes.py
│   └── utils
│       ├── __init__.py
│       └── security.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   └── test_users.py
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
   cd user-auth-system
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

Create a `.env` file in the root directory and define the following variables:
```
DATABASE_URL=<your_database_url>
SECRET_KEY=<your_secret_key>
```

## License

This project is licensed under the MIT License.