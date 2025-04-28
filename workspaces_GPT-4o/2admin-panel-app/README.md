# Admin Panel Application

This project is a Python web application that provides an administration panel. The panel dynamically receives parameters via URL and displays them in the interface, allowing for customization based on those parameters.

## Project Structure

```
admin-panel-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── routes
│   │   └── admin.py
│   └── utils
│       └── helpers.py
├── tests
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd admin-panel-app
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

5. **Run the application:**
   ```
   python app/main.py
   ```

## Usage

- Access the admin panel by navigating to `http://localhost:5000` in your web browser.
- You can customize the interface by passing parameters in the URL, for example: `http://localhost:5000/?param1=value1&param2=value2`.

## Testing

To run the tests, ensure your virtual environment is activated and execute:
```
pytest tests/
```

## License

This project is licensed under the MIT License.