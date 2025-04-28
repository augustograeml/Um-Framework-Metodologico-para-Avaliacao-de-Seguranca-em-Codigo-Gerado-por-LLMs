class FileService:
    def __init__(self, base_path):
        self.base_path = base_path

    def validate_file_name(self, file_name):
        # Basic validation to ensure the file name is safe
        if not file_name or '..' in file_name or '/' in file_name or '\\' in file_name:
            return False
        return True

    def get_file_path(self, file_name):
        if self.validate_file_name(file_name):
            return f"{self.base_path}/{file_name}"
        return None