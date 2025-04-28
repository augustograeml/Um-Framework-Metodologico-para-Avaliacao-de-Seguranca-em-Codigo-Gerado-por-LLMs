import unittest
from src.api.client import ApiClient

class TestApiClient(unittest.TestCase):

    def setUp(self):
        self.client = ApiClient()

    def test_fetch_data_valid_endpoint(self):
        # Assuming a mock endpoint that returns a known response
        endpoint = "https://jsonplaceholder.typicode.com/posts/1"
        response = self.client.fetch_data(endpoint)
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], 1)

    def test_fetch_data_invalid_endpoint(self):
        endpoint = "https://invalid-url.com"
        with self.assertRaises(Exception):
            self.client.fetch_data(endpoint)

    def test_fetch_data_empty_endpoint(self):
        endpoint = ""
        with self.assertRaises(ValueError):
            self.client.fetch_data(endpoint)

if __name__ == '__main__':
    unittest.main()