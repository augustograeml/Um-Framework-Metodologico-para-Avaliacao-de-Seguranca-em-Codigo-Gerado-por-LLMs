from flask import Flask
from app.database.connection import init_db
from app.auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    
    # Initialize database
    init_db(app)
    
    # Register authentication blueprint
    app.register_blueprint(auth_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)