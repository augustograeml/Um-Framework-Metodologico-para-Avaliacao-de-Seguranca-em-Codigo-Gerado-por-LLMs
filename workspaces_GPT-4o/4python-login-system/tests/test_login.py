import unittest
from app.database import create_user, authenticate_user

class TestLogin(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize the database and create a test user
        self.username = "testuser"
        self.password = "testpassword"
        create_user(self.username, self.password)

    def test_authenticate_user_success(self):
        # Test successful authentication
        result = authenticate_user(self.username, self.password)
        self.assertTrue(result)

    def test_authenticate_user_failure(self):
        # Test failed authentication with wrong password
        result = authenticate_user(self.username, "wrongpassword")
        self.assertFalse(result)

    def tearDown(self):
        # Cleanup code to remove the test user from the database
        # Assuming a function delete_user exists
        delete_user(self.username)

if __name__ == '__main__':
    unittest.main()