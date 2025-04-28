def verify_email_exists(email, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
    exists = cursor.fetchone()[0] > 0
    cursor.close()
    return exists

def get_user_by_email(email, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    return user