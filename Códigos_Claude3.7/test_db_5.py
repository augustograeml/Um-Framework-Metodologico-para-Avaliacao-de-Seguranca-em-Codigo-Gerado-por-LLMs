import unittest
import sqlite3
from app.database.db import get_db_connection

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    def test_insert_user(self):
        self.cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('test_user', 'test_password'))
        self.connection.commit()
        
        self.cursor.execute("SELECT * FROM users WHERE name = ?", ('test_user',))
        user = self.cursor.fetchone()
        
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'test_user')
        self.assertEqual(user[2], 'test_password')

    def test_query_user(self):
        self.cursor.execute("INSERT INTO users (name, password) VALUES (?, ?)", ('test_user', 'test_password'))
        self.connection.commit()
        
        self.cursor.execute("SELECT * FROM users WHERE name = ?", ('test_user',))
        user = self.cursor.fetchone()
        
        self.assertEqual(user[1], 'test_user')

if __name__ == '__main__':
    unittest.main()