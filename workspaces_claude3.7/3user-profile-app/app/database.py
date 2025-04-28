import sqlite3

def get_db_connection():
    conn = sqlite3.connect('instance/profiles.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bio TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, bio):
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, bio) VALUES (?, ?)', (name, bio))
    conn.commit()
    conn.close()

def update_user(user_id, name, bio):
    conn = get_db_connection()
    conn.execute('UPDATE users SET name = ?, bio = ? WHERE id = ?', (name, bio, user_id))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    return user

def get_all_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users

create_user_table()