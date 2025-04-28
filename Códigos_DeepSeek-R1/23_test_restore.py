import os
import pickle
import unittest
from src.backup_module.restore import RestoreManager

class TestRestoreManager(unittest.TestCase):

    def setUp(self):
        self.restore_manager = RestoreManager()
        self.test_file = 'test_object.pkl'
        self.test_object = {'key': 'value'}

        # Create a backup file for testing
        with open(self.test_file, 'wb') as f:
            pickle.dump(self.test_object, f)

    def tearDown(self):
        # Remove the test file after tests
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_restore_object(self):
        restored_object = self.restore_manager.restore_object(self.test_file)
        self.assertEqual(restored_object, self.test_object)

    def test_restore_non_existent_object(self):
        with self.assertRaises(FileNotFoundError):
            self.restore_manager.restore_object('non_existent_file.pkl')

    def test_list_restored_objects(self):
        self.restore_manager.restore_object(self.test_file)
        restored_objects = self.restore_manager.list_restored_objects()
        self.assertIn(self.test_object, restored_objects)

if __name__ == '__main__':
    unittest.main()