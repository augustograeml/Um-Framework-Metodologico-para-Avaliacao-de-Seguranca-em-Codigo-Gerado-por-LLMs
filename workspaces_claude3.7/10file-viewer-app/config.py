import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    FILE_STORAGE_PATH = os.path.join(BASE_DIR, 'app', 'files')
    MAX_FILE_SIZE = 16 * 1024 * 1024  # 16 MB
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}