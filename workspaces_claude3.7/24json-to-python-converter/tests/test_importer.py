import unittest
from src.converter.json_importer import JsonImporter

class TestJsonImporter(unittest.TestCase):
    def setUp(self):
        self.importer = JsonImporter()

    def test_import_json_valid(self):
        data = self.importer.import_json('data/sample.json')
        self.assertIsInstance(data, dict)
        self.assertIn('key', data)  # Replace 'key' with an actual key from your sample JSON

    def test_import_json_invalid(self):
        with self.assertRaises(FileNotFoundError):
            self.importer.import_json('data/non_existent_file.json')

    def test_import_json_empty(self):
        data = self.importer.import_json('data/empty.json')  # Assuming you have an empty.json for this test
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()