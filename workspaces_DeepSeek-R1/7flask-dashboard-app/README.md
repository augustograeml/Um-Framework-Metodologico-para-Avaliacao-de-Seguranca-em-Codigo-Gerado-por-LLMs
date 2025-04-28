# Flask Dashboard Application

This project is a Flask web application that includes a dashboard with user account settings functionality. Users can update their account settings through a form that submits data via POST.

## Project Structure

```
flask-dashboard-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── dashboard
│   │   │   └── account_settings.html
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   └── js
│   │       └── main.js
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

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

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Features

- User account settings form that allows users to update their information.
- Dashboard interface for managing user settings.
- Responsive design with CSS and JavaScript enhancements.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.