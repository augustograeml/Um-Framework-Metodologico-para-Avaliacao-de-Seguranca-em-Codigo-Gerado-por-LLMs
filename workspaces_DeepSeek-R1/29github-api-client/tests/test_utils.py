import unittest
from src.utils import print_repositories

class TestUtils(unittest.TestCase):

    def test_print_repositories(self):
        repos = [
            {"name": "repo1", "url": "http://github.com/user/repo1"},
            {"name": "repo2", "url": "http://github.com/user/repo2"}
        ]
        expected_output = "Repository: repo1, URL: http://github.com/user/repo1\n" \
                          "Repository: repo2, URL: http://github.com/user/repo2\n"
        
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print_repositories(repos)
            self.assertEqual(mock_stdout.getvalue(), expected_output)