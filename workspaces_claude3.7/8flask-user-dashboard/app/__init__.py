from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.auth.routes import auth as auth_blueprint
    from app.dashboard.routes import dashboard as dashboard_blueprint
    from app.profile.routes import profile as profile_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(profile_blueprint)

    return app