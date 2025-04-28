# File Viewer Application

This is a simple Flask application that allows users to view files stored on the server by entering the desired file name through an input field.

## Features

- User-friendly interface to input file names.
- Displays the contents of the requested file if it exists.
- Handles errors gracefully if the file is not found.

## Project Structure

```
file-viewer-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── file_utils.py
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── script.js
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd file-viewer-app
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Enter the desired file name in the input field and submit to view the file contents.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.