def verify_user_credentials(username, password):
    import sqlite3
    from database.db_operations import get_user_by_username

    user = get_user_by_username(username)
    if user and user['password'] == password:
        return True
    return False

def login_user(session, username):
    session['username'] = username

def logout_user(session):
    session.pop('username', None)