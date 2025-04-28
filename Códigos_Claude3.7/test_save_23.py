import os
import pickle
import unittest
from src.backup.save import save_object

class TestSaveObject(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_object.pkl'
        self.test_object = {'key': 'value', 'number': 42}

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_object(self):
        save_object(self.test_object, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_saved_object_content(self):
        save_object(self.test_object, self.test_file)
        with open(self.test_file, 'rb') as f:
            loaded_object = pickle.load(f)
        self.assertEqual(loaded_object, self.test_object)

    def test_save_empty_object(self):
        empty_object = {}
        save_object(empty_object, self.test_file)
        with open(self.test_file, 'rb') as f:
            loaded_object = pickle.load(f)
        self.assertEqual(loaded_object, empty_object)

if __name__ == '__main__':
    unittest.main()