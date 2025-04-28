import unittest
from app.auth.auth import Auth
from app.models.user import User

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth()
        self.test_user = User(id=1, username='testuser')
        self.auth.login(self.test_user)

    def test_login(self):
        self.assertTrue(self.auth.is_logged_in(self.test_user))

    def test_logout(self):
        self.auth.logout()
        self.assertFalse(self.auth.is_logged_in(self.test_user))

    def tearDown(self):
        self.auth.logout()

if __name__ == '__main__':
    unittest.main()