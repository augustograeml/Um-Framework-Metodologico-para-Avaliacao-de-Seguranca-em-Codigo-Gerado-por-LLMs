import unittest
import os
import pickle
from backup.restore import BackupRestorer

class TestBackupRestorer(unittest.TestCase):

    def setUp(self):
        self.restorer = BackupRestorer()
        self.test_filename = 'test_object.pkl'
        self.test_object = {'key': 'value'}

        # Save a test object to a file for restoration testing
        with open(self.test_filename, 'wb') as f:
            pickle.dump(self.test_object, f)

    def tearDown(self):
        # Remove the test file after tests
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_restore(self):
        restored_object = self.restorer.restore(self.test_filename)
        self.assertEqual(restored_object, self.test_object)

    def test_restore_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.restorer.restore('non_existent_file.pkl')

if __name__ == '__main__':
    unittest.main()