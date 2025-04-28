import unittest
from app.database.connection import connect_to_database
from app.search.query import search_by_name, search_by_email
from app.search.filters import filter_results

class TestUserSearch(unittest.TestCase):

    def setUp(self):
        self.connection = connect_to_database()
        self.test_data = [
            {'name': 'Alice Smith', 'email': 'alice@example.com'},
            {'name': 'Bob Johnson', 'email': 'bob@example.com'},
            {'name': 'Charlie Brown', 'email': 'charlie@example.com'}
        ]

    def test_search_by_name(self):
        results = search_by_name(self.test_data, 'Alice')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Alice Smith')

    def test_search_by_email(self):
        results = search_by_email(self.test_data, 'bob@example.com')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['email'], 'bob@example.com')

    def test_filter_results(self):
        results = filter_results(self.test_data, name='Charlie')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], 'Charlie Brown')

    def tearDown(self):
        self.connection.close()

if __name__ == '__main__':
    unittest.main()