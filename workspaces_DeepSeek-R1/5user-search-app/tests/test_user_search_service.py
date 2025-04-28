import unittest
from services.user_search_service import UserSearchService
from models.user import User

class TestUserSearchService(unittest.TestCase):

    def setUp(self):
        self.user_search_service = UserSearchService()
        self.user_search_service.users = [
            User(id=1, name="Alice Smith", email="alice@example.com"),
            User(id=2, name="Bob Johnson", email="bob@example.com"),
            User(id=3, name="Charlie Brown", email="charlie@example.com"),
        ]

    def test_search_by_name(self):
        results = self.user_search_service.search_by_name("Alice")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Alice Smith")

        results = self.user_search_service.search_by_name("Bob")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Bob Johnson")

        results = self.user_search_service.search_by_name("Nonexistent")
        self.assertEqual(len(results), 0)

    def test_search_by_email(self):
        results = self.user_search_service.search_by_email("alice@example.com")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email, "alice@example.com")

        results = self.user_search_service.search_by_email("bob@example.com")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].email, "bob@example.com")

        results = self.user_search_service.search_by_email("nonexistent@example.com")
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()