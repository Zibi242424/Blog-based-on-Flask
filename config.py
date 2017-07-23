# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xa4\x9c\xf2D\x9d\xcd\x19%a\xe5\xfco\x08d|0\xb3u\xfaX\xc3\x13\xd5\xf8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
