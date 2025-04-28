from flask import Flask

app = Flask(__name__)

from app.routes import transfer

app.register_blueprint(transfer.bp)