import unittest
from config_system.saver import Saver

class TestSaver(unittest.TestCase):

    def setUp(self):
        self.saver = Saver()
        self.test_config = {'key': 'value'}

    def test_save_config(self):
        file_path = 'test_config.json'
        self.saver.save_config(file_path, self.test_config)
        saved_configs = self.saver.get_saved_configs()
        self.assertIn(file_path, saved_configs)

    def test_get_saved_configs(self):
        file_path1 = 'config1.json'
        file_path2 = 'config2.json'
        self.saver.save_config(file_path1, self.test_config)
        self.saver.save_config(file_path2, self.test_config)
        saved_configs = self.saver.get_saved_configs()
        self.assertEqual(len(saved_configs), 2)
        self.assertIn(file_path1, saved_configs)
        self.assertIn(file_path2, saved_configs)

if __name__ == '__main__':
    unittest.main()