import unittest
from app.auth.models import User
from app.auth.utils import hash_password
from app.database.connection import get_db_connection

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.connection = get_db_connection()
        self.test_user = User(username='testuser', password_hash=hash_password('testpassword'))
        self.connection.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                                (self.test_user.username, self.test_user.password_hash))
        self.connection.commit()

    def tearDown(self):
        self.connection.execute("DELETE FROM users WHERE username = ?", (self.test_user.username,))
        self.connection.commit()
        self.connection.close()

    def test_user_registration(self):
        user = User(username='newuser', password_hash=hash_password('newpassword'))
        self.connection.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                                (user.username, user.password_hash))
        self.connection.commit()
        
        result = self.connection.execute("SELECT * FROM users WHERE username = ?", (user.username,)).fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['username'], user.username)

    def test_user_login(self):
        user = User(username='testuser', password_hash=hash_password('testpassword'))
        result = self.connection.execute("SELECT * FROM users WHERE username = ?", (user.username,)).fetchone()
        self.assertIsNotNone(result)
        self.assertTrue(user.verify_password('testpassword'))

if __name__ == '__main__':
    unittest.main()