from flask import Flask
from app.routes.download_routes import download_routes

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(download_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)