class User:
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def create_user(cls, username, password_hash):
        # Logic to create a user in the database
        pass

    @classmethod
    def get_user_by_username(cls, username):
        # Logic to retrieve a user from the database by username
        pass

    @classmethod
    def get_user_by_id(cls, user_id):
        # Logic to retrieve a user from the database by user ID
        pass