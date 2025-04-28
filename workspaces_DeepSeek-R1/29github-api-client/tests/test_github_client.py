import unittest
from unittest.mock import patch, MagicMock
from src.github_client import GitHubClient

class TestGitHubClient(unittest.TestCase):

    @patch('src.github_client.requests.get')
    def test_authenticate(self, mock_get):
        client = GitHubClient()
        client.token = 'test_token'
        mock_get.return_value.status_code = 200
        
        result = client.authenticate()
        
        self.assertTrue(result)
        mock_get.assert_called_once_with('https://api.github.com/user', headers={'Authorization': 'token test_token'})

    @patch('src.github_client.requests.get')
    def test_get_user_repositories(self, mock_get):
        client = GitHubClient()
        client.token = 'test_token'
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        
        repos = client.get_user_repositories('test_user')
        
        self.assertEqual(len(repos), 2)
        self.assertEqual(repos[0]['name'], 'repo1')
        mock_get.assert_called_once_with('https://api.github.com/users/test_user/repos', headers={'Authorization': 'token test_token'})

    @patch('src.github_client.requests.get')
    def test_get_user_repositories_not_found(self, mock_get):
        client = GitHubClient()
        client.token = 'test_token'
        mock_get.return_value.status_code = 404
        
        repos = client.get_user_repositories('non_existent_user')
        
        self.assertEqual(repos, [])
        mock_get.assert_called_once_with('https://api.github.com/users/non_existent_user/repos', headers={'Authorization': 'token test_token'})

if __name__ == '__main__':
    unittest.main()