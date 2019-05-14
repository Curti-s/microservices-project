import os


class BaseConfig:
    """
    Base Configuration
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 13
    
class DevelopmentConfig(BaseConfig):
    """
    Development config
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    BCRYPT_LOG_ROUNDS = 4

class TestingConfig(BaseConfig):
    """
    Testing config
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
    BCRYPT_LOG_ROUNDS = 4

class ProductionConfig(BaseConfig):
    """
    Production config
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')