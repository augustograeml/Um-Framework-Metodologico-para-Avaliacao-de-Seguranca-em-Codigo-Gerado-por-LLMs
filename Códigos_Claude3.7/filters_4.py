def filter_by_name(users, name):
    if not name:
        return users
    return [user for user in users if name.lower() in user['name'].lower()]

def filter_by_email(users, email):
    if not email:
        return users
    return [user for user in users if email.lower() in user['email'].lower()]

def dynamic_filter(users, name=None, email=None):
    filtered_users = filter_by_name(users, name)
    filtered_users = filter_by_email(filtered_users, email)
    return filtered_users