import unittest
from app.services.file_service import save_file, allowed_file

class TestFileService(unittest.TestCase):

    def test_allowed_file(self):
        self.assertTrue(allowed_file('test.pdf'))
        self.assertTrue(allowed_file('image.jpg'))
        self.assertFalse(allowed_file('document.txt'))
        self.assertFalse(allowed_file('archive.zip'))

    def test_save_file(self):
        # Assuming a mock file object is created for testing
        class MockFile:
            def save(self, path):
                return True

        mock_file = MockFile()
        result = save_file(mock_file, 'uploads/test.pdf')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()