import unittest
from app.services.http_client import HttpClient
from unittest.mock import patch

class TestHttpClient(unittest.TestCase):

    @patch('app.services.http_client.requests.get')
    def test_get_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'response data'
        
        client = HttpClient()
        response = client.get('http://example.com')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'response data')
        mock_get.assert_called_once_with('http://example.com')

    @patch('app.services.http_client.requests.post')
    def test_post_request(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.text = 'created'
        
        client = HttpClient()
        response = client.post('http://example.com', data={'key': 'value'})
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.text, 'created')
        mock_post.assert_called_once_with('http://example.com', data={'key': 'value'})

if __name__ == '__main__':
    unittest.main()