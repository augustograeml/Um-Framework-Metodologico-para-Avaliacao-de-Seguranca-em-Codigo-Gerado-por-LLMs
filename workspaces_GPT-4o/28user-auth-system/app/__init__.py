from flask import Flask

app = Flask(__name__)

# App-level configurations can be set here
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.auth.routes import auth as auth_blueprint
app.register_blueprint(auth_blueprint)