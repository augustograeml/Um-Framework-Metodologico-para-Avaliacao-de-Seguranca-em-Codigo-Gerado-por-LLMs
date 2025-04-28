def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_strong_password(password):
    return (len(password) >= 8 and 
            any(char.isdigit() for char in password) and 
            any(char.isupper() for char in password) and 
            any(char.islower() for char in password) and 
            any(char in "!@#$%^&*()-_+=<>?{}[]|:;'" for char in password))