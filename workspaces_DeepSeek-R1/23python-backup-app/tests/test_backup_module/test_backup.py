import os
import unittest
from src.backup_module.backup import BackupManager

class TestBackupManager(unittest.TestCase):

    def setUp(self):
        self.backup_manager = BackupManager()
        self.test_object = {'key': 'value'}
        self.test_filename = 'test_backup.pkl'

    def tearDown(self):
        # Clean up any created backup files
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_object(self):
        self.backup_manager.save_object(self.test_object, self.test_filename)
        self.assertTrue(os.path.exists(self.test_filename))

    def test_list_backups(self):
        self.backup_manager.save_object(self.test_object, self.test_filename)
        backups = self.backup_manager.list_backups()
        self.assertIn(self.test_filename, backups)

    def test_save_object_overwrite(self):
        self.backup_manager.save_object(self.test_object, self.test_filename)
        new_object = {'new_key': 'new_value'}
        self.backup_manager.save_object(new_object, self.test_filename)
        # Check if the file still exists after overwrite
        self.assertTrue(os.path.exists(self.test_filename))

if __name__ == '__main__':
    unittest.main()