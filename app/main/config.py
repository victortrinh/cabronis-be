import os

basedir = os.path.abspath(os.path.dirname(__file__))

stream = os.popen('heroku config:get DATABASE_URL -a pscbreaks')
output = stream.read()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ghghuvtusdalshurhtycakydiriybae')
    DEBUG = False


class DevelopmentConfig(Config):
    S3_ACCESS_KEY_ID = 'AKIAJCDZTGIOZBPQE5EQ'
    S3_BUCKET_NAME = 'pscbreaks-bucket'
    S3_PREFIX_NAME = 'public/images/'
    S3_SECRET_ACCESS_KEY = '4cj8I9n1heJeu2LDHUEkyBlSttHcIHil+YCCideL'
    S3_URL = 'https://pscbreaks-bucket.s3.amazonaws.com'
    DEBUG = True
    DISABLE_AUTHENTICATION = True
    IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    IMAGE_MAX_FILE_SIZE = 2  # In Megabytes
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/cabronis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/cabronis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


class ProductionConfig(Config):
    S3_ACCESS_KEY_ID = 'AKIAJCDZTGIOZBPQE5EQ'
    S3_BUCKET_NAME = 'pscbreaks-bucket'
    S3_PREFIX_NAME = 'public/images/'
    S3_SECRET_ACCESS_KEY = '4cj8I9n1heJeu2LDHUEkyBlSttHcIHil+YCCideL'
    S3_URL = 'https://pscbreaks-bucket.s3.amazonaws.com'
    DEBUG = False
    DISABLE_AUTHENTICATION = False
    IMAGE_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    IMAGE_MAX_FILE_SIZE = 2  # In Megabytes
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or output
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
