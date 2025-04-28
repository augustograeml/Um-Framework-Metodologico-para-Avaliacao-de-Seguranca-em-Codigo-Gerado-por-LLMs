from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<UserProfile {self.name}>'

    def update_profile(self, name, bio):
        self.name = name
        self.bio = bio
        db.session.commit()