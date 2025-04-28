# Python Login System

This project is a simple login system built with Python that utilizes an SQLite database to store user credentials. Users can enter their username and password to access the platform. 

## Features

- User registration and login functionality
- Secure password storage using hashing
- SQLite database for storing user credentials
- Simple command-line interface for user interaction

## Project Structure

```
python-login-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── utils.py
├── migrations
│   └── README.md
├── tests
│   ├── __init__.py
│   └── test_login.py
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
   cd python-login-system
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

Follow the prompts to register or log in to the system.

## Testing

To run the tests, use the following command:
```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.