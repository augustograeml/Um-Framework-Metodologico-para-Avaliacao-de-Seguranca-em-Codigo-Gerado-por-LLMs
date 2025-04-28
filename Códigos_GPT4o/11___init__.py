from flask import Flask

app = Flask(__name__)

from app.routes import download

# Additional application setup code can go here if needed.