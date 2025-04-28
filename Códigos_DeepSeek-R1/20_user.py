class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def save(self):
        # Code to save user data to the database
        pass

    @staticmethod
    def get_user_by_id(user_id):
        # Code to retrieve user data from the database by user_id
        pass