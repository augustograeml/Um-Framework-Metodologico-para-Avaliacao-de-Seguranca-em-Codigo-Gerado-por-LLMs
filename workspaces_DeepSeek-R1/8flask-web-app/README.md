# Flask Web Application

This project is a Flask web application that includes a user authentication system, a dashboard, and a profile view where users can change their email.

## Features

- User registration and login
- Protected dashboard and profile views
- Ability to change user email

## Project Structure

```
flask-web-app
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── templates
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   └── profile.html
│   ├── static
│   │   └── css
│   │       └── main.css
│   └── utils.py
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-web-app
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

## Usage

1. Set up the configuration in `config.py` as needed.
2. Run the application:
   ```
   python run.py
   ```
3. Access the application in your web browser at `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License.