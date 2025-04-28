# Password Update System

This project is a simple password update system that allows users to modify their passwords by providing their registered email. The application is built using Flask and utilizes a database to store user information securely.

## Project Structure

```
password-update-system
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── services
│   │   ├── __init__.py
│   │   └── password_service.py
│   └── utils
│       ├── __init__.py
│       └── email_validator.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd password-update-system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Configure the application:**
   Update the `config.py` file with your database connection details.

## Usage

To run the application, execute the following command:

```
python app/main.py
```

The application will start, and you can access it at `http://localhost:5000`.

## Features

- User can update their password by providing their registered email.
- Password validation to ensure security.
- Email format validation to ensure the provided email is registered.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.