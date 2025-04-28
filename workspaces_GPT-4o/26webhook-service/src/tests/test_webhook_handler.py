import unittest
from src.services.webhook_handler import WebhookHandler
from unittest.mock import patch

class TestWebhookHandler(unittest.TestCase):

    @patch('src.utils.http_client.HttpClient.get')
    def test_handle_webhook_success(self, mock_get):
        mock_get.return_value = 'Success'
        handler = WebhookHandler()
        response = handler.handle_webhook('http://example.com')
        self.assertEqual(response, 'Success')
        mock_get.assert_called_once_with('http://example.com')

    @patch('src.utils.http_client.HttpClient.get')
    def test_handle_webhook_failure(self, mock_get):
        mock_get.side_effect = Exception('Request failed')
        handler = WebhookHandler()
        with self.assertRaises(Exception):
            handler.handle_webhook('http://example.com')
        mock_get.assert_called_once_with('http://example.com')

    @patch('src.utils.http_client.HttpClient.post')
    def test_handle_webhook_post(self, mock_post):
        mock_post.return_value = 'Posted Successfully'
        handler = WebhookHandler()
        response = handler.handle_webhook('http://example.com', method='POST', data={'key': 'value'})
        self.assertEqual(response, 'Posted Successfully')
        mock_post.assert_called_once_with('http://example.com', {'key': 'value'})

    @patch('src.utils.http_client.HttpClient.post')
    def test_handle_webhook_post_failure(self, mock_post):
        mock_post.side_effect = Exception('Post failed')
        handler = WebhookHandler()
        with self.assertRaises(Exception):
            handler.handle_webhook('http://example.com', method='POST', data={'key': 'value'})
        mock_post.assert_called_once_with('http://example.com', {'key': 'value'})

if __name__ == '__main__':
    unittest.main()