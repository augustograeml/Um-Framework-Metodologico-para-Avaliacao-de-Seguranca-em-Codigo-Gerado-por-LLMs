from flask import Flask
from app.api.routes import register_routes
from app.auth.security import configure_security

def create_app():
    app = Flask(__name__)
    
    configure_security(app)
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)