# Log Analysis Application

This project is a web application designed for log analysis. It allows users to search for specific terms within log files and view the results in a user-friendly interface.

## Features

- Upload log files for analysis.
- Search for specific terms within the logs.
- View detailed results of the search.
- User-friendly web interface.

## Project Structure

```
log-analysis-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── log_analyzer
│   │   ├── __init__.py
│   │   ├── analyzer.py
│   │   ├── parser.py
│   │   └── search.py
│   ├── models
│   │   ├── __init__.py
│   │   └── log_entry.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── web_routes.py
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   └── js
│   │       └── search.js
│   └── templates
│       ├── base.html
│       ├── index.html
│       └── results.html
├── tests
│   ├── __init__.py
│   ├── test_analyzer.py
│   └── test_search.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd log-analysis-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app/main.py
   ```
2. Open your web browser and go to `http://localhost:5000` to access the application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.