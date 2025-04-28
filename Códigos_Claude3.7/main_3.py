from flask import Flask
from app.database import init_db
from app.routes.profile import profile_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    app.register_blueprint(profile_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)