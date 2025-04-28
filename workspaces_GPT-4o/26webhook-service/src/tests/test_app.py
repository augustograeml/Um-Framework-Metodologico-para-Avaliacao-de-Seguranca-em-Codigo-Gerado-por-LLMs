import unittest
from app import app

class WebhookServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_webhook_post(self):
        response = self.app.post('/webhook', json={'url': 'http://example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Webhook received', response.data)

    def test_webhook_post_invalid_url(self):
        response = self.app.post('/webhook', json={'url': 'invalid-url'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid URL', response.data)

if __name__ == '__main__':
    unittest.main()