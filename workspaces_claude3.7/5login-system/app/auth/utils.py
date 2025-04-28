import bcrypt

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verifies a provided password against the stored hashed password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))