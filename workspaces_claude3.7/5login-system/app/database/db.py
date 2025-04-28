import sqlite3

def get_db_connection():
    conn = sqlite3.connect('app/database/users.db')
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result