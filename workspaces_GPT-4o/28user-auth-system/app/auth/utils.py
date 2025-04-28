def hash_password(password: str) -> str:
    from werkzeug.security import generate_password_hash
    return generate_password_hash(password)

def verify_password(stored_password: str, provided_password: str) -> bool:
    from werkzeug.security import check_password_hash
    return check_password_hash(stored_password, provided_password)

def generate_token(user_id: int) -> str:
    import jwt
    import datetime
    secret_key = "your_secret_key"  # Replace with your actual secret key
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({'user_id': user_id, 'exp': expiration}, secret_key, algorithm='HS256')
    return token

def decode_token(token: str) -> dict:
    import jwt
    secret_key = "your_secret_key"  # Replace with your actual secret key
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'error': 'Invalid token'}