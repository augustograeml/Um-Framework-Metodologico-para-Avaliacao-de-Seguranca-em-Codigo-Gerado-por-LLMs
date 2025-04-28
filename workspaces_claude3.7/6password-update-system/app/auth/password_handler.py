from werkzeug.security import generate_password_hash, check_password_hash
from app.database.db_connector import get_user_by_email, update_user_password

def hash_password(password):
    return generate_password_hash(password)

def verify_password(plain_password, hashed_password):
    return check_password_hash(hashed_password, plain_password)

def update_password(email, new_password):
    user = get_user_by_email(email)
    if user:
        hashed_password = hash_password(new_password)
        update_user_password(email, hashed_password)
        return True
    return False