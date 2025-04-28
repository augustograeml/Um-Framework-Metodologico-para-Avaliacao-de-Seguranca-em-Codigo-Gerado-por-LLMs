import unittest
from src.engine.sandbox import Sandbox

class TestSandbox(unittest.TestCase):

    def setUp(self):
        self.sandbox = Sandbox()

    def test_validate_script_valid(self):
        script = "print('Hello, World!')"
        self.assertTrue(self.sandbox.validate_script(script))

    def test_validate_script_invalid(self):
        script = "import os; os.system('rm -rf /')"
        self.assertFalse(self.sandbox.validate_script(script))

    def test_run_script_valid(self):
        script = "print('Test script')"
        result = self.sandbox.run_script(script)
        self.assertIn("Test script", result)

    def test_run_script_invalid(self):
        script = "1 / 0"  # This will raise a ZeroDivisionError
        with self.assertRaises(Exception):
            self.sandbox.run_script(script)

if __name__ == '__main__':
    unittest.main()