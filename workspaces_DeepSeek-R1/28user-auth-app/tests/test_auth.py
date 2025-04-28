import unittest
from app.auth.auth import UserAuth
from app.database.db import get_db_session
from app.auth.models import User

class TestUserAuth(unittest.TestCase):

    def setUp(self):
        self.auth = UserAuth()
        self.session = get_db_session()

    def tearDown(self):
        self.session.close()

    def test_register_user(self):
        username = "testuser"
        password = "testpassword"
        result = self.auth.register(username, password)
        self.assertTrue(result)
        user = self.session.query(User).filter_by(username=username).first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)

    def test_login_user(self):
        username = "testuser"
        password = "testpassword"
        self.auth.register(username, password)
        result = self.auth.login(username, password)
        self.assertTrue(result)

    def test_login_invalid_user(self):
        result = self.auth.login("invaliduser", "wrongpassword")
        self.assertFalse(result)

    def test_register_existing_user(self):
        username = "testuser"
        password = "testpassword"
        self.auth.register(username, password)
        result = self.auth.register(username, password)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()