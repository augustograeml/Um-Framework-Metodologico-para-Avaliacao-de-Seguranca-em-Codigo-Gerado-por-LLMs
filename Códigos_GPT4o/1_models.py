from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Comment {self.id} by {self.username}>'