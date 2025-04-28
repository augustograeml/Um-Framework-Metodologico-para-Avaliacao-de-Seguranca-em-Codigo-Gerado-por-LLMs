# Flask Admin Panel

This project is a simple Flask web application that provides an administration panel. The panel is capable of receiving parameters via URL and dynamically displaying them in the interface, allowing for customization based on those parameters.

## Project Structure

```
flask-admin-panel
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── admin.html
│   └── static
│       └── style.css
├── config.py
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-admin-panel
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
   pip install Flask
   ```

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/admin?param1=value1&param2=value2` to access the admin panel. Replace `param1` and `param2` with your desired parameters.

## Customization

You can customize the appearance of the admin panel by modifying the `app/static/style.css` file. The parameters received via the URL can be used to dynamically change the content displayed in the `app/templates/admin.html` file.

## Contributing

Feel free to submit issues or pull requests to improve the project.