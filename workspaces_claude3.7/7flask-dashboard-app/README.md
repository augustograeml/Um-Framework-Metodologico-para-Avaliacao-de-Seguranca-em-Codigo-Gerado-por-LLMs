# Flask Dashboard Application

This is a Flask web application that provides a dashboard interface with user account settings functionality. The application allows users to manage their account settings through a user-friendly form.

## Project Structure

```
flask-dashboard-app
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── forms
│   │   ├── __init__.py
│   │   └── account_settings.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   └── settings.py
│   ├── static
│   │   ├── css
│   │   │   ├── main.css
│   │   │   └── dashboard.css
│   │   └── js
│   │       └── form_validation.js
│   └── templates
│       ├── base.html
│       ├── auth
│       │   ├── login.html
│       │   └── register.html
│       ├── dashboard
│       │   └── index.html
│       └── settings
│           └── account.html
├── migrations
│   └── __init__.py
├── .env.example
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Features

- User authentication (login and registration)
- Dashboard view displaying user-specific information
- Account settings form for updating user information
- Client-side form validation

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-dashboard-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up the environment variables by copying `.env.example` to `.env` and updating the values as needed.

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be accessible at `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.