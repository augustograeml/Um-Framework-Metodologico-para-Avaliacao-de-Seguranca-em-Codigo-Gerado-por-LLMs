from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from .routes import auth, blog, comments
        app.register_blueprint(auth.bp)
        app.register_blueprint(blog.bp)
        app.register_blueprint(comments.bp)

    return app