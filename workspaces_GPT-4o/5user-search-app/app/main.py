from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.search import search_bp

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)