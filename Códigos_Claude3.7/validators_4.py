def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_valid_name(name):
    return isinstance(name, str) and len(name) > 0

def validate_search_criteria(name, email):
    if name and not is_valid_name(name):
        raise ValueError("Invalid name format.")
    if email and not is_valid_email(email):
        raise ValueError("Invalid email format.")
    return True