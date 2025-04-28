# Flask User Dashboard

This project is a web application built with Flask that provides a user dashboard and profile visualization. Users can log in to access their dashboard and profile, where they can update their email and view relevant information.

## Features

- User authentication (login, registration, logout)
- Dashboard for authenticated users
- Profile page for viewing and updating user information
- Responsive design with CSS styling
- JavaScript functionality for enhanced user experience

## Project Structure

```
flask-user-dashboard
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── dashboard
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── profile
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   │   ├── main.css
│   │   │   └── dashboard.css
│   │   └── js
│   │       ├── main.js
│   │       └── profile.js
│   └── templates
│       ├── auth
│       │   ├── login.html
│       │   └── register.html
│       ├── dashboard
│       │   └── index.html
│       ├── profile
│       │   └── index.html
│       ├── base.html
│       └── home.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-user-dashboard
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

1. Set up the database and configuration in `config.py`.
2. Run the application:
   ```
   python run.py
   ```
3. Access the application in your web browser at `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.