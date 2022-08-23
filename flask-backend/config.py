import os

class BaseConfig(object):
    API_PREFIX = '/api'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TESTING = False
    DEBUG = False


class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
