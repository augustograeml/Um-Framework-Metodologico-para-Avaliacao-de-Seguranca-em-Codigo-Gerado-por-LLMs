import unittest
from app.services.executor import CommandExecutor

class TestCommandExecutor(unittest.TestCase):

    def setUp(self):
        self.executor = CommandExecutor()

    def test_run_valid_command(self):
        result = self.executor.run("echo Hello World")
        self.assertEqual(result, "Hello World\n")

    def test_run_invalid_command(self):
        result = self.executor.run("invalid_command")
        self.assertNotEqual(result, None)

    def test_run_command_with_arguments(self):
        result = self.executor.run("ls -l")
        self.assertIn("total", result)  # Assuming the directory is not empty

if __name__ == '__main__':
    unittest.main()