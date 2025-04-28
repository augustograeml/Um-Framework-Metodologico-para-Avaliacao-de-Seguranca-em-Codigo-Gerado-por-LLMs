import unittest
from src.engine.script_executor import ScriptExecutor

class TestScriptExecutor(unittest.TestCase):

    def setUp(self):
        self.executor = ScriptExecutor()

    def test_execute_script(self):
        script = "print('Hello, World!')"
        result = self.executor.execute_script(script)
        self.assertEqual(result, "Hello, World!")

    def test_list_available_scripts(self):
        available_scripts = self.executor.list_available_scripts()
        self.assertIsInstance(available_scripts, list)

if __name__ == '__main__':
    unittest.main()