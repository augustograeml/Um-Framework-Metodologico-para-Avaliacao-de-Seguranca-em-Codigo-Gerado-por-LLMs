import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))  # 16 MB
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')