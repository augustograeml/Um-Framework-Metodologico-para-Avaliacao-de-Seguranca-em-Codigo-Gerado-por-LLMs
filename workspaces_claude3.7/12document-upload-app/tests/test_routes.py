import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_upload_page(self):
        response = self.client.get('/upload')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload a Document', response.data)

    def test_file_upload(self):
        with open('tests/test_file.txt', 'w') as f:
            f.write('This is a test file.')

        with open('tests/test_file.txt', 'rb') as f:
            response = self.client.post('/upload', data={'file': f})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'File uploaded successfully', response.data)

    def test_file_upload_invalid(self):
        response = self.client.post('/upload', data={'file': ''})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'No file part', response.data)

    def test_upload_page_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go to Upload', response.data)