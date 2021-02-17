import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'ghghuvtusdalshurhtycakydiriybae'
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
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/cabronis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
