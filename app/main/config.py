import os

basedir = os.path.abspath(os.path.dirname(__file__))

stream = os.popen('heroku config:get DATABASE_URL -a pscbreaks')
output = stream.read()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ghghuvtusdalshurhtycakydiriybae')
    DEBUG = False


class DevelopmentConfig(Config):
    BUCKETEER_ACCESS_KEY_ID = 'AKIAVZH4SBSY3BJ4ECKV'
    BUCKETEER_BUCKET_NAME = 'bucketeer-87788d9b-831a-4c5b-a8c8-161fd2c57dfa'
    BUCKETEER_PREFIX_NAME = ' public/images/'
    BUCKETEER_SECRET_ACCESS_KEY = '0DcRc2eoUU0i83sN3QPrMvFHtTInmEaNw35L5CpW'
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
    BUCKETEER_ACCESS_KEY_ID = 'AKIAVZH4SBSY3BJ4ECKV'
    BUCKETEER_BUCKET_NAME = 'bucketeer-87788d9b-831a-4c5b-a8c8-161fd2c57dfa'
    BUCKETEER_PREFIX_NAME = ' public/images/'
    BUCKETEER_SECRET_ACCESS_KEY = '0DcRc2eoUU0i83sN3QPrMvFHtTInmEaNw35L5CpW'
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
