import unittest
from unittest.mock import patch, MagicMock
from src.api.github_client import GitHubClient

class TestGitHubClient(unittest.TestCase):

    @patch('src.api.github_client.requests.get')
    def test_authenticate(self, mock_get):
        token = 'test_token'
        client = GitHubClient()
        client.authenticate(token)

        self.assertEqual(client.token, token)
        self.assertEqual(mock_get.call_count, 0)  # No call should be made during authentication

    @patch('src.api.github_client.requests.get')
    def test_get_user_repositories(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {'name': 'repo1', 'html_url': 'http://github.com/user/repo1', 'description': 'Test repo 1'},
            {'name': 'repo2', 'html_url': 'http://github.com/user/repo2', 'description': 'Test repo 2'}
        ]
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        client = GitHubClient()
        client.authenticate('test_token')
        repos = client.get_user_repositories('user')

        self.assertEqual(len(repos), 2)
        self.assertEqual(repos[0]['name'], 'repo1')
        self.assertEqual(repos[1]['name'], 'repo2')
        mock_get.assert_called_once_with('https://api.github.com/users/user/repos', headers={'Authorization': 'token test_token'})

    @patch('src.api.github_client.requests.get')
    def test_get_user_repositories_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        client = GitHubClient()
        client.authenticate('test_token')
        repos = client.get_user_repositories('nonexistent_user')

        self.assertEqual(repos, [])
        mock_get.assert_called_once_with('https://api.github.com/users/nonexistent_user/repos', headers={'Authorization': 'token test_token'})

if __name__ == '__main__':
    unittest.main()