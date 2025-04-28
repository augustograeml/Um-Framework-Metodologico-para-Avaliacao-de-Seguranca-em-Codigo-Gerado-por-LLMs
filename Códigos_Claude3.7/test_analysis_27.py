import unittest
from src.api_integration.analysis import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = DataAnalyzer()

    def test_analyze(self):
        test_data = {'key1': 10, 'key2': 20}
        expected_result = {'key1': 10, 'key2': 20, 'total': 30}  # Example expected result
        result = self.analyzer.analyze(test_data)
        self.assertEqual(result, expected_result)

    def test_generate_report(self):
        analysis_results = {'total': 30}
        expected_report = "Total: 30"  # Example expected report
        report = self.analyzer.generate_report(analysis_results)
        self.assertEqual(report, expected_report)

if __name__ == '__main__':
    unittest.main()