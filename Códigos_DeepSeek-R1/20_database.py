def connect_to_db():
    import sqlite3
    connection = sqlite3.connect('users.db')
    return connection

def execute_query(query, params=()):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    connection.close()