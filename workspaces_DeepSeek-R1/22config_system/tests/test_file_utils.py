import unittest
from src.utils.file_utils import read_json, write_json
import os

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_config.json'
        self.test_data = {'key': 'value'}

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_write_json(self):
        write_json(self.test_file_path, self.test_data)
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_read_json(self):
        write_json(self.test_file_path, self.test_data)
        data = read_json(self.test_file_path)
        self.assertEqual(data, self.test_data)

    def test_read_json_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json('non_existent_file.json')

    def test_write_json_invalid_data(self):
        with self.assertRaises(TypeError):
            write_json(self.test_file_path, set([1, 2, 3]))  # Invalid data type for JSON

if __name__ == '__main__':
    unittest.main()