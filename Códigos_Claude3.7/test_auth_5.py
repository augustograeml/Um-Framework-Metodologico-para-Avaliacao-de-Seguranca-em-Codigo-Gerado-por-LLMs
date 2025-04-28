import unittest
from app.auth.models import User
from app.database.db import get_db_connection

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.connection = get_db_connection()
        self.user = User(self.connection)

    def tearDown(self):
        self.connection.close()

    def test_create_user(self):
        username = "testuser"
        password = "testpassword"
        self.user.create(username, password)
        retrieved_user = self.user.get(username)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['username'], username)

    def test_verify_password(self):
        username = "testuser"
        password = "testpassword"
        self.user.create(username, password)
        self.assertTrue(self.user.verify_password(username, password))
        self.assertFalse(self.user.verify_password(username, "wrongpassword"))

    def test_user_not_found(self):
        retrieved_user = self.user.get("nonexistentuser")
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()