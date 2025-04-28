# Login System

This project implements a login system that requires users to enter a numeric verification code before accessing their accounts. 

## Features

- User authentication with username and password.
- Numeric verification code generation and validation.
- Logging of authentication events.
- Database integration for user data management.

## Project Structure

```
login-system
├── src
│   ├── main.py               # Entry point of the application
│   ├── auth                  # Authentication module
│   │   ├── __init__.py
│   │   ├── login.py          # User login functionality
│   │   └── verification.py    # Verification code functionality
│   ├── database              # Database module
│   │   ├── __init__.py
│   │   └── db_handler.py     # Database handling functionality
│   └── utils                 # Utility functions
│       ├── __init__.py
│       └── helpers.py        # Helper functions for the application
├── requirements.txt          # Project dependencies
├── .gitignore                # Files and directories to ignore by Git
└── README.md                 # Project documentation
```

## Setup Instructions

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

4. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Users can log in using their username and password.
- Upon successful authentication, a numeric verification code will be generated and sent to the user's registered email.
- Users must enter the verification code to gain access to their accounts.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.