import pytest


import config as config
from api import create_app
from database.models import *



@pytest.fixture
def app():
    app = create_app(config.TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client



