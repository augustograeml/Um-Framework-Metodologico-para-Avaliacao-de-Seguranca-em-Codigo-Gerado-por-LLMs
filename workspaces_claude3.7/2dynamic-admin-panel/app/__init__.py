from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize extensions here if any

    # Register blueprints
    from app.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app