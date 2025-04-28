from flask import json
from app import create_app
import unittest

class TestWebhookAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_webhook_post_valid_url(self):
        response = self.client.post('/webhook', json={'url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', json.loads(response.data))

    def test_webhook_post_invalid_url(self):
        response = self.client.post('/webhook', json={'url': 'invalid-url'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', json.loads(response.data))

    def test_webhook_post_missing_url(self):
        response = self.client.post('/webhook', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()