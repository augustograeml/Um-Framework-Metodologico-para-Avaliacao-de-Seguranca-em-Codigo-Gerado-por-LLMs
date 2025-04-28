# Login System

This project is a simple login system built using Python and Flask. It allows users to register and log in using their credentials, which are securely stored in an SQLite database.

## Features

- User registration with name and password
- User authentication
- Password hashing for security
- SQLite database for storing user credentials

## Project Structure

```
login-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── schema.sql
│   └── config.py
├── tests
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_db.py
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
   cd login-system
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
2. Access the application in your web browser at `http://127.0.0.1:5000`.

## Testing

To run the tests, use the following command:
```
pytest
```

## License

This project is licensed under the MIT License.