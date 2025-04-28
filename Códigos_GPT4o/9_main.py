from flask import Flask
from app.routes.transfer import transfer_bp

def create_app():
    app = Flask(__name__)
    
    # Load configurations from environment variables or a config file
    app.config.from_pyfile('.env', silent=True)

    # Register blueprints
    app.register_blueprint(transfer_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)