import os
from dotenv import load_dotenv
import uuid

load_dotenv()


class Config:
    SECRET_KEY = uuid.uuid4().hex
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST_TEST')}:3306/{os.environ.get('DATABASE_NAME_TEST')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get('FLASK_APP')
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST')}:3306/{os.environ.get('DATABASE_NAME')}"
