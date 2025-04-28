class UserSearchService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def search_by_name(self, name):
        query = "SELECT * FROM users WHERE name LIKE %s"
        with self.db_connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, ('%' + name + '%',))
            results = cursor.fetchall()
        return results

    def search_by_email(self, email):
        query = "SELECT * FROM users WHERE email LIKE %s"
        with self.db_connection.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, ('%' + email + '%',))
            results = cursor.fetchall()
        return results