class Loader:
    def __init__(self):
        self.config = None

    def load_config(self, file_path):
        with open(file_path, 'r') as file:
            self.config = file.read()  # Assuming the config is in a text format

    def get_config(self):
        return self.config