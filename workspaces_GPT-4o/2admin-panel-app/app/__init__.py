from flask import Flask

app = Flask(__name__)

from app.routes import admin  # Import routes after initializing the app to avoid circular imports