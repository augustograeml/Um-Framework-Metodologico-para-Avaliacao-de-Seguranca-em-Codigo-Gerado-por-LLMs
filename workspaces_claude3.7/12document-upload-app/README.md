# Document Upload Application

This is a simple web application that allows users to upload documents to the server. The application is built using Flask, a lightweight WSGI web application framework in Python.

## Features

- User authentication (login and registration)
- File upload functionality
- File validation and storage
- Basic front-end interface

## Project Structure

```
document-upload-app
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── upload.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services
│   │   ├── __init__.py
│   │   └── file_service.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── upload.js
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── upload.html
│   └── uploads
│       └── .gitkeep
├── tests
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_file_service.py
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd document-upload-app
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

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the application to register, log in, and upload documents.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.