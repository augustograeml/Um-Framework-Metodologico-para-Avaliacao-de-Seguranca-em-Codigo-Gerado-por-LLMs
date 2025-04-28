from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import main as routes

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)