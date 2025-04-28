from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from app.models import User
from app.utils.email_validator import is_valid_email

db = SQLAlchemy()

def update_password(email, new_password):
    if not is_valid_email(email):
        return "Invalid email format."

    user = User.query.filter_by(email=email).first()
    if user is None:
        return "Email not registered."

    user.password = generate_password_hash(new_password)
    db.session.commit()
    return "Password updated successfully."