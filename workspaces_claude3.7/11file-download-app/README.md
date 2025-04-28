# File Download Application

This is a Python web application that allows users to download reports by providing the file name. The application is built using Flask and follows a modular structure for easy maintenance and scalability.

## Project Structure

```
file-download-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── download_routes.py
│   ├── services
│   │   ├── __init__.py
│   │   └── file_service.py
│   ├── models
│   │   ├── __init__.py
│   │   └── report.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── download.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── main.js
├── data
│   └── reports
│       └── .gitkeep
├── tests
│   ├── __init__.py
│   └── test_download.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd file-download-app
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

6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- On the main page, enter the name of the report file you wish to download.
- If the file exists, it will be downloaded to your device.

## Testing

To run the tests, ensure your virtual environment is activated and execute:
```
pytest tests/
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.