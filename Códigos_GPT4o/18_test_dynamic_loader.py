import unittest
import importlib
import sys
import os

from app.loader.dynamic_loader import DynamicLoader

class TestDynamicLoader(unittest.TestCase):

    def setUp(self):
        self.loader = DynamicLoader()
        self.test_lib_name = "test_library"
        self.test_lib_path = os.path.join(os.path.dirname(__file__), self.test_lib_name + ".py")

        # Create a simple test library file
        with open(self.test_lib_path, 'w') as f:
            f.write("def test_function():\n")
            f.write("    return 'Test function executed'\n")

    def tearDown(self):
        # Clean up the test library file after tests
        if os.path.exists(self.test_lib_path):
            os.remove(self.test_lib_path)

    def test_load_library(self):
        self.loader.load_library(self.test_lib_name)
        test_lib = importlib.import_module(self.test_lib_name)
        self.assertTrue(hasattr(test_lib, 'test_function'))

    def test_unload_library(self):
        self.loader.load_library(self.test_lib_name)
        self.loader.unload_library(self.test_lib_name)
        with self.assertRaises(ModuleNotFoundError):
            importlib.import_module(self.test_lib_name)

if __name__ == '__main__':
    unittest.main()