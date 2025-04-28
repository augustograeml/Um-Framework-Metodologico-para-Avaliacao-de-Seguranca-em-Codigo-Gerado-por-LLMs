import unittest
from app import main

class TestPasswordUpdateAPI(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_update_password_success(self):
        response = self.app.post('/api/update-password', json={
            'email': 'user@example.com',
            'new_password': 'NewSecurePassword123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Password updated successfully', response.get_data(as_text=True))

    def test_update_password_user_not_found(self):
        response = self.app.post('/api/update-password', json={
            'email': 'nonexistent@example.com',
            'new_password': 'NewSecurePassword123'
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn('User not found', response.get_data(as_text=True))

    def test_update_password_invalid_email(self):
        response = self.app.post('/api/update-password', json={
            'email': 'invalid-email',
            'new_password': 'NewSecurePassword123'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_data(as_text=True))

    def test_update_password_missing_fields(self):
        response = self.app.post('/api/update-password', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email and new password are required', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()