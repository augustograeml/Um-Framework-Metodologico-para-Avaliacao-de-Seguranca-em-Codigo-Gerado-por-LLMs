import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///site.db'
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if os.environ.get('ALLOWED_HOSTS') else []
    # Add any additional configuration settings here as needed.