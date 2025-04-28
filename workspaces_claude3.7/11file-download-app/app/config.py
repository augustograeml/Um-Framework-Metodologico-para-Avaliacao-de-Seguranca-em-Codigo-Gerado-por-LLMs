import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    REPORTS_DIR = os.path.join(BASE_DIR, '..', 'data', 'reports')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit file size to 16 MB
    ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx'}  # Example allowed file types
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')  # Replace with your secret key for production