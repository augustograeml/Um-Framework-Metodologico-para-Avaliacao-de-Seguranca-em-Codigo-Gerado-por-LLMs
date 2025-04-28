class LogSearcher:
    def __init__(self, log_entries):
        self.log_entries = log_entries

    def search_terms(self, term):
        return [entry for entry in self.log_entries if term in entry.message]

    def get_results(self, term):
        results = self.search_terms(term)
        return results if results else "No results found."