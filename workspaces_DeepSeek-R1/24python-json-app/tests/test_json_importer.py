import json
import os
import unittest
from src.utils.json_importer import import_json

class TestJsonImporter(unittest.TestCase):

    def setUp(self):
        self.valid_json_path = os.path.join(os.path.dirname(__file__), '../data/sample.json')
        self.invalid_json_path = os.path.join(os.path.dirname(__file__), '../data/invalid_sample.json')

    def test_import_valid_json(self):
        data = import_json(self.valid_json_path)
        self.assertIsInstance(data, list)  # Assuming the JSON data is a list of objects
        self.assertGreater(len(data), 0)   # Ensure that data is not empty

    def test_import_invalid_json(self):
        with self.assertRaises(json.JSONDecodeError):
            import_json(self.invalid_json_path)

    def test_import_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            import_json('non_existent_file.json')

if __name__ == '__main__':
    unittest.main()