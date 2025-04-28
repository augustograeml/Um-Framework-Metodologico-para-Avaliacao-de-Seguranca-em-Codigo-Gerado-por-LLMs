class FileManager:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def save_file(self, file_name, content):
        with open(f"{self.storage_path}/{file_name}", "wb") as file:
            file.write(content)

    def retrieve_file(self, file_name):
        with open(f"{self.storage_path}/{file_name}", "rb") as file:
            return file.read()

    def file_exists(self, file_name):
        import os
        return os.path.isfile(f"{self.storage_path}/{file_name}")