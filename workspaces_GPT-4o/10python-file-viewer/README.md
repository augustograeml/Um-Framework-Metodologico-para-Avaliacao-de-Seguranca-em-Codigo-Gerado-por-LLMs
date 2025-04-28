# Python File Viewer

## Overview
The Python File Viewer is a simple web application that allows users to view files stored on the server by entering the desired file name. Built using Flask, this application provides a user-friendly interface for file retrieval.

## Features
- Input field for users to enter the file name.
- Displays the content of the requested file if it exists.
- Error handling for non-existent files.

## Project Structure
```
python-file-viewer
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   └── styles.css
│   └── utils
│       └── file_handler.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd python-file-viewer
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app/main.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Enter the desired file name in the input field and submit to view the file content.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.