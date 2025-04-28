import unittest
from app.database.connection import connect_to_database, disconnect_from_database
from app.database.models import User

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.connection = connect_to_database()

    def tearDown(self):
        disconnect_from_database(self.connection)

    def test_connection(self):
        self.assertIsNotNone(self.connection)

    def test_user_model(self):
        user = User(name="Test User", email="test@example.com")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")

    def test_user_creation(self):
        user = User(name="New User", email="newuser@example.com")
        # Assuming there's a method to save the user to the database
        user.save()
        self.assertIsNotNone(user.id)  # Assuming the user model has an id attribute

    def test_user_retrieval(self):
        user = User(name="Retrieve User", email="retrieve@example.com")
        user.save()
        retrieved_user = User.get_by_email("retrieve@example.com")  # Assuming a method to retrieve user by email
        self.assertEqual(retrieved_user.name, "Retrieve User")

if __name__ == '__main__':
    unittest.main()