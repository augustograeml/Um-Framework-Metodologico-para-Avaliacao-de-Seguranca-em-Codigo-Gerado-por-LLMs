from flask import Flask
from app.database.db_connector import init_db
from app.api.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)