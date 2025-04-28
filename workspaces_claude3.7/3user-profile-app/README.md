# User Profile Application

This is a simple user profile application built with Python and Flask. It allows users to create and manage their profiles, including updating their name and bio.

## Features

- User profile creation and management
- Update user name and bio
- Data stored in an SQLite database

## Project Structure

```
user-profile-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── profile.py
│   ├── forms
│   │   ├── __init__.py
│   │   └── profile.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── profile
│   │       ├── edit.html
│   │       └── view.html
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   ├── database.py
│   └── config.py
├── instance
│   └── profiles.db
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd user-profile-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app/main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. You can create a new profile or update your existing profile through the provided forms.

## License

This project is licensed under the MIT License.