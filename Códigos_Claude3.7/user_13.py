class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In a real application, this should be hashed

    def check_password(self, password):
        return self.password == password  # In a real application, use a secure method to check

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password  # Do not expose password in production
        }