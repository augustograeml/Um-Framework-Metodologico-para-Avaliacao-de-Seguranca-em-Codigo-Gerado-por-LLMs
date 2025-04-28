# Log Analysis Application

This project is a web application that allows users to analyze log files by searching for specific terms. It is built using Flask, a lightweight WSGI web application framework in Python.

## Features

- Search for specific terms in log files.
- View results in a user-friendly interface.
- Simple and intuitive design.

## Project Structure

```
log_analysis_app
├── app.py               # Main entry point of the application
├── requirements.txt     # Dependencies for the project
├── README.md            # Documentation for the project
├── static               # Static files (CSS)
│   └── style.css        # Styles for the web application
├── templates            # HTML templates
│   └── index.html       # Main page template
└── logs                 # Sample log files
    └── sample.log       # Sample log file for testing
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd log_analysis_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

- Enter a search term in the input field and submit the form to search through the log entries.
- The results will be displayed on the same page.

## License

This project is licensed under the MIT License.