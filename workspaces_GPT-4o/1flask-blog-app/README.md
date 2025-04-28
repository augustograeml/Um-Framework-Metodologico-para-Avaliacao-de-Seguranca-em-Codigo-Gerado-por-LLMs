# Flask Blog Application

This is a simple Flask blog application that allows users to submit and view comments. The application is structured to separate concerns, making it easy to maintain and extend.

## Project Structure

```
flask-blog-app
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application routes
│   ├── forms.py             # Contains form classes for user input
│   ├── models.py            # Defines data models for the application
│   ├── templates             # Contains HTML templates
│   │   ├── base.html        # Base template for the application
│   │   ├── index.html       # Template for the blog index page
│   │   └── comments.html     # Template for displaying individual comments
│   └── static               # Contains static files
│       ├── css              # CSS styles
│       │   └── styles.css   # Styles for the application
│       └── js               # JavaScript files
│           └── scripts.js    # Client-side functionality
├── migrations                # Migration scripts for database changes
├── tests                     # Unit tests for the application
│   ├── __init__.py          # Initializes the test module
│   └── test_routes.py       # Unit tests for the routes
├── .env                      # Environment variables for the application
├── .gitignore                # Files and directories to ignore by version control
├── config.py                 # Configuration settings for the application
├── requirements.txt          # Lists dependencies required for the project
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-blog-app
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

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up the environment variables:**
   Create a `.env` file in the root directory and add your configuration settings.

6. **Run the application:**
   ```
   flask run
   ```

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser to view the blog.
- Users can submit comments through the provided form, and all comments will be displayed on the index page.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.