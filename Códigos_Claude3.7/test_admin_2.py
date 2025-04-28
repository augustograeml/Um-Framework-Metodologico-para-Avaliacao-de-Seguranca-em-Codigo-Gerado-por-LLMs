import unittest
from app import create_app

class AdminPanelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_admin_dashboard(self):
        response = self.client.get('/admin/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Dashboard', response.data)

    def test_parameter_view(self):
        response = self.client.get('/admin/parameter_view?param1=value1&param2=value2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Parameter View', response.data)
        self.assertIn(b'value1', response.data)
        self.assertIn(b'value2', response.data)

    def test_invalid_parameter(self):
        response = self.client.get('/admin/parameter_view?invalid_param=value')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No valid parameters provided', response.data)

if __name__ == '__main__':
    unittest.main()