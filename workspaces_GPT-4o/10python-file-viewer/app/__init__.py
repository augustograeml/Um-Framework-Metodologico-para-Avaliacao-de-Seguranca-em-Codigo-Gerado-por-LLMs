from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config['SECRET_KEY'] = 'your_secret_key'  # Example configuration

from app import main  # Importing the main module to register routes