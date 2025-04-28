# Flask File Viewer

This project is a simple Flask application that allows users to view files stored on the server by entering the desired file name through an input field.

## Project Structure

```
flask-file-viewer
├── app.py               # Main entry point of the Flask application
├── templates            # Directory for HTML templates
│   └── index.html      # User interface template
├── static              # Directory for static files (CSS, JS, etc.)
│   └── style.css       # CSS styles for the application
├── files               # Directory where files to be viewed are stored
│   └── (files)         # Place your files here
├── requirements.txt     # List of dependencies for the project
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-file-viewer
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

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Enter the desired file name in the input field and submit to view the file content.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.