import unittest
from api_integration.client import APIClient

class TestAPIClient(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_data(self):
        endpoint = "https://api.example.com/data"
        response = self.client.get_data(endpoint)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

    def test_post_data(self):
        endpoint = "https://api.example.com/data"
        data = {"key": "value"}
        response = self.client.post_data(endpoint, data)
        self.assertIsNotNone(response)
        self.assertEqual(response.get("status"), "success")

if __name__ == '__main__':
    unittest.main()