class FileLoader:
    def load(self, file_path):
        """Load configuration from a file."""
        with open(file_path, 'r') as file:
            return file.read()

    def save(self, file_path, data):
        """Save configuration to a file."""
        with open(file_path, 'w') as file:
            file.write(data)