# Login System

This project is a simple login system built using Python and Flask. It allows users to enter their name and password to access the platform. User credentials are stored in an SQLite database.

## Project Structure

```
login_system
├── app.py
├── database
│   ├── __init__.py
│   └── db_operations.py
├── auth
│   ├── __init__.py
│   └── auth_operations.py
├── templates
│   └── login.html
├── static
│   └── style.css
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd login_system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the login page.

## Usage Guidelines

- Users can register by entering their name and password.
- The system will validate the credentials and allow access to the platform upon successful login.
- Ensure that the SQLite database is properly set up before running the application.

## License

This project is licensed under the MIT License.