# Python Web Application

This project is a web application built using Flask that includes a dashboard and profile visualization. Users can log in to access their dashboard and profile, where they can update their email address.

## Features

- User authentication (login and registration)
- Dashboard for authenticated users
- Profile page for viewing and updating user information

## Project Structure

```
python-web-app
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── dashboard
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── profile
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── templates
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── dashboard.html
│   │   └── profile.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd python-web-app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

## Authentication

Users must register and log in to access the dashboard and profile pages. The authentication system is built using Flask-WTF for form handling.

## License

This project is licensed under the MIT License.