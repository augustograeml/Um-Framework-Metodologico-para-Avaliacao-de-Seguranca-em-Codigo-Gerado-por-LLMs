# settings.py

import os

class Settings:
    API_TITLE = "URL Downloader API"
    API_VERSION = "1.0.0"
    STORAGE_PATH = os.getenv("STORAGE_PATH", "./downloads")
    MAX_DOWNLOAD_SIZE = int(os.getenv("MAX_DOWNLOAD_SIZE", 10485760))  # 10 MB default
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

settings = Settings()