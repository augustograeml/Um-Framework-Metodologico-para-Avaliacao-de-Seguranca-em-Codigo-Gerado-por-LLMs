import unittest
from src.api.github_client import GitHubClient

class TestGitHubClient(unittest.TestCase):

    def setUp(self):
        self.client = GitHubClient()
        self.client.token = 'test_token'  # Mock token for testing

    def test_authenticate(self):
        self.client.authenticate()
        self.assertIsNotNone(self.client.session)
        self.assertEqual(self.client.session.headers['Authorization'], 'token test_token')

    def test_get_user_repositories(self):
        self.client.authenticate()
        repositories = self.client.get_user_repositories('octocat')  # Example user
        self.assertIsInstance(repositories, list)

    def test_handle_api_response_success(self):
        response = {'status_code': 200, 'data': []}
        result = self.client.handle_api_response(response)
        self.assertEqual(result, response['data'])

    def test_handle_api_response_error(self):
        response = {'status_code': 404, 'message': 'Not Found'}
        with self.assertRaises(Exception) as context:
            self.client.handle_api_response(response)
        self.assertTrue('Not Found' in str(context.exception))

if __name__ == '__main__':
    unittest.main()