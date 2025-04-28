import unittest
import json
from src.services.json_importer import JsonImporter

class TestJsonImporter(unittest.TestCase):

    def setUp(self):
        self.importer = JsonImporter()

    def test_import_valid_json(self):
        json_data = '{"name": "John", "age": 30}'
        with open('test_valid.json', 'w') as f:
            f.write(json_data)
        
        result = self.importer.import_json('test_valid.json')
        expected = {'name': 'John', 'age': 30}
        self.assertEqual(result, expected)

    def test_import_invalid_json(self):
        json_data = '{"name": "John", "age": 30'
        with open('test_invalid.json', 'w') as f:
            f.write(json_data)
        
        with self.assertRaises(ValueError):
            self.importer.import_json('test_invalid.json')

    def tearDown(self):
        import os
        try:
            os.remove('test_valid.json')
            os.remove('test_invalid.json')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()