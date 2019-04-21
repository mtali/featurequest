import os

# grab base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__)))


class Config:
    """Base configuration class"""
    # this key should be set as an environment variables, otherwise we user
    # the default provided (not recommended)
    SECRET_KEY = os.environ.get('SECRET_KEY') or "1724b9bfa333fc60f2cc6d71eb03cdcd"
    SQLALCHEMY_COMMIT_ON_TEAR_DOWN = True
    FEATUREQUEST_SUBJECT_PREFIX = '[featurequest]'
    FEATUREQUEST_MAIL_SENDER = 'FEATUREQUEST <featurequest@admin.com>'
    FEATUREQUEST_ADMIN = os.environ.get('FEATUREQUEST_ADMIN')

    @staticmethod
    def init_app(app):
        """Configuration specific initialization here! """
        pass


class DevelopmentConfig(Config):
    """Development specific configurations"""
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data-dev.sqlite')


class TestingConfig(Config):
    """Testing specific configurations"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data-test.sqlite')


class ProductionConfig(Config):
    """Testing specific configurations"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
