from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auth import auth as auth_blueprint
    from app.routes.dashboard import dashboard as dashboard_blueprint
    from app.routes.settings import settings as settings_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(settings_blueprint)

    return app