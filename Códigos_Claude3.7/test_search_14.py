import unittest
from app.log_analyzer.search import LogSearcher

class TestLogSearcher(unittest.TestCase):

    def setUp(self):
        self.log_searcher = LogSearcher()
        self.sample_entries = [
            {"timestamp": "2023-10-01 12:00:00", "level": "INFO", "message": "User logged in"},
            {"timestamp": "2023-10-01 12:05:00", "level": "ERROR", "message": "Failed to load resource"},
            {"timestamp": "2023-10-01 12:10:00", "level": "INFO", "message": "User logged out"},
        ]
        self.log_searcher.entries = self.sample_entries

    def test_search_terms_found(self):
        results = self.log_searcher.search_terms("logged")
        self.assertEqual(len(results), 2)
        self.assertIn(self.sample_entries[0], results)
        self.assertIn(self.sample_entries[2], results)

    def test_search_terms_not_found(self):
        results = self.log_searcher.search_terms("nonexistent")
        self.assertEqual(len(results), 0)

    def test_search_terms_case_insensitive(self):
        results = self.log_searcher.search_terms("ERROR")
        self.assertEqual(len(results), 1)
        self.assertIn(self.sample_entries[1], results)

if __name__ == '__main__':
    unittest.main()