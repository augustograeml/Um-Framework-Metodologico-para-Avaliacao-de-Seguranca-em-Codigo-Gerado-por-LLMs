# Flask Blog Application

This is a simple Flask blog application that allows users to submit and view comments. The application is structured to provide a clean separation of concerns, with dedicated files for routes, models, forms, and templates.

## Project Structure

```
flask-blog-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── comments.html
│   └── static
│       └── style.css
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-blog-app
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

2. Open your web browser and go to `http://127.0.0.1:5000` to view the application.

## Features

- Submit comments through a form.
- View a list of submitted comments.
- Simple and clean user interface.

## License

This project is licensed under the MIT License.