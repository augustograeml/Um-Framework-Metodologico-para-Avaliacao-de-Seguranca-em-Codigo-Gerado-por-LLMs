class User:
    def __init__(self, id, name, bio):
        self.id = id
        self.name = name
        self.bio = bio

    def update_profile(self, new_name, new_bio):
        self.name = new_name
        self.bio = new_bio

    @staticmethod
    def get_user_by_id(user_id, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(id=user_data[0], name=user_data[1], bio=user_data[2])
        return None

    def save_to_db(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (id, name, bio) VALUES (?, ?, ?)", 
                       (self.id, self.name, self.bio))
        db_connection.commit()