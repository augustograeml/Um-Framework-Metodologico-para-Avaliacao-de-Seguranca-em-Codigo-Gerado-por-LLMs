from flask import Flask

app = Flask(__name__)

from app.routes import download_routes

app.register_blueprint(download_routes.bp)