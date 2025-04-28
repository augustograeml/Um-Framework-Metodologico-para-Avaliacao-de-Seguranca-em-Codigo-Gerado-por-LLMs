import unittest
from src.utils.auth import validate_aws_credentials

class TestAuth(unittest.TestCase):

    def test_valid_credentials(self):
        # Assuming valid credentials are set in the environment
        self.assertTrue(validate_aws_credentials())

    def test_invalid_credentials(self):
        # Set invalid credentials for testing
        # This would typically involve mocking or setting environment variables
        self.assertFalse(validate_aws_credentials())

if __name__ == '__main__':
    unittest.main()