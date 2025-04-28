import unittest
from src.auth.login import LoginHandler
from src.models.user import User

class TestLoginHandler(unittest.TestCase):

    def setUp(self):
        self.login_handler = LoginHandler()
        self.test_user = User(username="testuser", password="password123")
        self.login_handler.register_user(self.test_user)

    def test_login_success(self):
        result = self.login_handler.login_user("testuser", "password123")
        self.assertTrue(result)

    def test_login_failure(self):
        result = self.login_handler.login_user("testuser", "wrongpassword")
        self.assertFalse(result)

    def test_logout(self):
        self.login_handler.login_user("testuser", "password123")
        result = self.login_handler.logout_user("testuser")
        self.assertTrue(result)

    def tearDown(self):
        self.login_handler.logout_user("testuser")

if __name__ == '__main__':
    unittest.main()