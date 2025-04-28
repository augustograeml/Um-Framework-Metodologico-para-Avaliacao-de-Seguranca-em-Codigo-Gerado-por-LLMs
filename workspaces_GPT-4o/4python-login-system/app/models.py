class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
        db_connection.commit()

    @staticmethod
    def find_by_username(db_connection, username):
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()