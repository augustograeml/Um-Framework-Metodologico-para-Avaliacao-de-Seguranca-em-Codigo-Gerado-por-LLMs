import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', 'logs/application.log')
    SEARCH_RESULTS_LIMIT = int(os.getenv('SEARCH_RESULTS_LIMIT', 100))
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///logs.db')