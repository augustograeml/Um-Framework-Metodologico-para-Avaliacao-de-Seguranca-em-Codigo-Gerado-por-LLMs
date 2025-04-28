class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    DATABASE_URI = 'sqlite:///your_database.db'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    STATIC_URL = '/static/'
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user:password@localhost/prod_db'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev_db.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///test_db.db'