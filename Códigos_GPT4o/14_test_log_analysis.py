import unittest
from app.services.log_analysis import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()
        self.sample_logs = [
            "Error: Unable to connect to database",
            "Warning: Low disk space",
            "Info: User logged in",
            "Error: File not found",
            "Info: User logged out"
        ]
        self.analyzer.load_logs(self.sample_logs)

    def test_search_logs_found(self):
        results = self.analyzer.search_logs("Error")
        self.assertEqual(len(results), 2)
        self.assertIn("Error: Unable to connect to database", results)
        self.assertIn("Error: File not found", results)

    def test_search_logs_not_found(self):
        results = self.analyzer.search_logs("Success")
        self.assertEqual(len(results), 0)

    def test_search_logs_case_insensitive(self):
        results = self.analyzer.search_logs("info")
        self.assertEqual(len(results), 2)
        self.assertIn("Info: User logged in", results)
        self.assertIn("Info: User logged out", results)

if __name__ == '__main__':
    unittest.main()