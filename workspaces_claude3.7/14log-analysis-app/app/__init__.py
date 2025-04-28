from flask import Flask

app = Flask(__name__)

from app.routes.web_routes import setup_routes

setup_routes(app)