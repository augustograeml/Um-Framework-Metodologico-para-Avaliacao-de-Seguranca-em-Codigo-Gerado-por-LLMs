from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config['DEBUG'] = True

from app.routes import *  # Import routes to register them with the app