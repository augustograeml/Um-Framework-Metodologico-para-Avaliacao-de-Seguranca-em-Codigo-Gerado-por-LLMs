class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file

    def search_logs(self, term):
        results = []
        with open(self.log_file, 'r') as file:
            for line in file:
                if term in line:
                    results.append(line.strip())
        return results