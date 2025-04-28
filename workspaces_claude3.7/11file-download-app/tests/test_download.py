import unittest
from app import create_app

class DownloadTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_download_file(self):
        response = self.client.get('/download?filename=test_report.pdf')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Content-Disposition', response.headers)
        self.assertIn('attachment; filename=test_report.pdf', response.headers['Content-Disposition'])

    def test_download_nonexistent_file(self):
        response = self.client.get('/download?filename=nonexistent_report.pdf')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()