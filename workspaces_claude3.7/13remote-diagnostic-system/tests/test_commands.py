import unittest
from app.commands.executor import CommandExecutor

class TestCommandExecutor(unittest.TestCase):
    
    def setUp(self):
        self.executor = CommandExecutor()

    def test_run_valid_command(self):
        result = self.executor.run("echo Hello World")
        self.assertEqual(result.stdout.strip(), "Hello World")
        self.assertEqual(result.returncode, 0)

    def test_run_invalid_command(self):
        result = self.executor.run("invalid_command")
        self.assertNotEqual(result.returncode, 0)

    def test_run_command_with_arguments(self):
        result = self.executor.run("ls -l")
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()