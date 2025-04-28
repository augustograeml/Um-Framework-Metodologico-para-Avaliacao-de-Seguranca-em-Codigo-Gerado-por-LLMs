import unittest
from app.log_analyzer.analyzer import LogAnalyzer
from app.models.log_entry import LogEntry

class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = LogAnalyzer()
        self.sample_logs = [
            LogEntry(timestamp="2023-10-01 12:00:00", level="INFO", message="Test log entry 1"),
            LogEntry(timestamp="2023-10-01 12:01:00", level="ERROR", message="Test log entry 2"),
            LogEntry(timestamp="2023-10-01 12:02:00", level="DEBUG", message="Test log entry 3"),
        ]

    def test_analyze_logs(self):
        result = self.analyzer.analyze_logs(self.sample_logs)
        self.assertIsInstance(result, dict)
        self.assertIn("INFO", result)
        self.assertIn("ERROR", result)
        self.assertIn("DEBUG", result)

    def test_get_summary(self):
        self.analyzer.analyze_logs(self.sample_logs)
        summary = self.analyzer.get_summary()
        self.assertEqual(summary["INFO"], 1)
        self.assertEqual(summary["ERROR"], 1)
        self.assertEqual(summary["DEBUG"], 1)

if __name__ == '__main__':
    unittest.main()