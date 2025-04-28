import unittest
from app.auth.verification import Verification
from app.models.user import User

class TestVerification(unittest.TestCase):

    def setUp(self):
        self.verification = Verification()
        self.user = User(id=1, username='testuser')

    def test_send_verification_code(self):
        result = self.verification.send_verification_code(self.user)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 6)  # Assuming the code is 6 digits long

    def test_verify_code_success(self):
        code = self.verification.send_verification_code(self.user)
        result = self.verification.verify_code(self.user, code)
        self.assertTrue(result)

    def test_verify_code_failure(self):
        result = self.verification.verify_code(self.user, '123456')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()