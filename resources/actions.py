from flask_restful import Api

from resources.routers import *
from .auth import *


def register_actions(app):
    api = Api(app)

