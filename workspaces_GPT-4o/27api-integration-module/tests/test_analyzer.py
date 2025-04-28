import unittest
from src.analysis.analyzer import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = DataAnalyzer()

    def test_analyze_empty_data(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result, "No data to analyze.")

    def test_analyze_valid_data(self):
        data = [1, 2, 3, 4, 5]
        result = self.analyzer.analyze(data)
        self.assertEqual(result, {
            'mean': 3.0,
            'sum': 15,
            'count': 5
        })

    def test_analyze_invalid_data(self):
        data = ["a", "b", "c"]
        with self.assertRaises(ValueError):
            self.analyzer.analyze(data)

if __name__ == '__main__':
    unittest.main()