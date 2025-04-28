import unittest
import os
import pickle
from backup.save import BackupSaver

class TestBackupSaver(unittest.TestCase):

    def setUp(self):
        self.saver = BackupSaver()
        self.test_file = 'test_object.pkl'
        self.test_object = {'key': 'value'}

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save(self):
        self.saver.save(self.test_object, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load(self):
        self.saver.save(self.test_object, self.test_file)
        loaded_object = self.saver.load(self.test_file)
        self.assertEqual(loaded_object, self.test_object)

    def test_load_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.saver.load('non_existent_file.pkl')

if __name__ == '__main__':
    unittest.main()