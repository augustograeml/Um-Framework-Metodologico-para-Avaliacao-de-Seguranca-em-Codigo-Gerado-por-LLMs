from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('config.Config')

    # Register blueprints
    from .routes import auth, transfers
    app.register_blueprint(auth.bp)
    app.register_blueprint(transfers.bp)

    return app