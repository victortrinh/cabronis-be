from flask import Blueprint
from flask_cors import CORS
from flask_restplus import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.image_controller import api as image_ns
from .main.controller.pack_controller import api as pack_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.wishlist_controller import api as wishlist_ns

BASE_URL = '/api'

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Cabronis',
          version='1.0.0',
          description='All servicing for Cabronis',
          authorizations={
              'Bearer': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              }
          }
          )

api.blueprint.after_request


def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')


api.add_namespace(user_ns, path=BASE_URL + '/user')
api.add_namespace(auth_ns, path=BASE_URL + '/auth')
api.add_namespace(pack_ns, path=BASE_URL + '/pack')
api.add_namespace(wishlist_ns, path=BASE_URL + '/wishlist')
api.add_namespace(image_ns, path=BASE_URL + '/image')

CORS(api.blueprint)
