import os
import pickle
import unittest
from src.backup.restore import restore_object

class TestRestoreObject(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_object.pkl'
        self.test_object = {'key': 'value', 'number': 42}
        with open(self.test_file, 'wb') as f:
            pickle.dump(self.test_object, f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_restore_object(self):
        restored_object = restore_object(self.test_file)
        self.assertEqual(restored_object, self.test_object)

    def test_restore_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            restore_object('non_existent_file.pkl')

    def test_restore_corrupted_file(self):
        with open(self.test_file, 'wb') as f:
            f.write(b'corrupted data')
        with self.assertRaises(pickle.UnpicklingError):
            restore_object(self.test_file)

if __name__ == '__main__':
    unittest.main()