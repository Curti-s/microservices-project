class BaseConfig:
    """
    Base Configuration
    """
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    """
    Development config
    """
    DEBUG = True

class TestingConfig(BaseConfig):
    """
    Testing config
    """
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """
    Production config
    """
    DEBUG = False
    