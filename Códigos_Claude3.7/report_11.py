class Report:
    def __init__(self, filename, description):
        self.filename = filename
        self.description = description

    def get_filename(self):
        return self.filename

    def get_description(self):
        return self.description

    def __repr__(self):
        return f"<Report(filename={self.filename}, description={self.description})>"