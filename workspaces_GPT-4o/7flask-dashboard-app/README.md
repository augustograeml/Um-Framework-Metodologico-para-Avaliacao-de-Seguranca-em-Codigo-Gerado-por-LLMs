# Flask Dashboard Application

## Overview
This project is a Flask web application that provides a user dashboard with account settings functionality. Users can view their dashboard and update their account information through a settings form.

## Project Structure
```
flask-dashboard-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   └── settings.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   └── forms.py
├── instance
│   └── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd flask-dashboard-app
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

5. **Configure the application**:
   Update the `instance/config.py` file with your configuration settings, such as secret keys or database configurations.

## Running the Application
To run the application, execute the following command:
```
python run.py
```
The application will start on `http://127.0.0.1:5000/`.

## Usage
- Navigate to the dashboard to view user information.
- Access the settings page to update your account information. The form submits data via POST to the server for processing.

## License
This project is licensed under the MIT License.