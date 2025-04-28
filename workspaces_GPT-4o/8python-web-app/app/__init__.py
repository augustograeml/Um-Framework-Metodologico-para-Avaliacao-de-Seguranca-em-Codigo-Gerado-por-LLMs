from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from app.profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    return app