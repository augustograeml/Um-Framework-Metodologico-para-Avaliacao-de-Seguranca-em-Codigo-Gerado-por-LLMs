def hash_password(password):
    from werkzeug.security import generate_password_hash
    return generate_password_hash(password)

def check_password(hashed_password, password):
    from werkzeug.security import check_password_hash
    return check_password_hash(hashed_password, password)

def is_authenticated(user):
    return user.is_authenticated

def get_user_email(user):
    return user.email

def update_user_email(user, new_email):
    user.email = new_email
    # Here you would typically add code to commit the change to the database
    return user