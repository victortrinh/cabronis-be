import os
import psycopg2

basedir = os.path.abspath(os.path.dirname(__file__))

stream = os.popen('heroku config:get DATABASE_URL -a pscbreaks')
output = stream.read()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ghghuvtusdalshurhtycakydiriybae')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    DISABLE_AUTHENTICATION = True
    IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    IMAGE_MAX_FILE_SIZE = 2  # In Megabytes
    IMAGE_UPLOAD_DIRECTORY = 'app\\static\\images'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/cabronis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/cabronis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    DISABLE_AUTHENTICATION = False
    IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    IMAGE_MAX_FILE_SIZE = 2  # In Megabytes
    IMAGE_UPLOAD_DIRECTORY = 'app\\static\\images'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or output
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
