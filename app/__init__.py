from flask import Blueprint
from flask_cors import CORS
from flask_restplus import Api

from app.main.controller.packs.basketball_pack_controller import api as basketball_pack_ns
from app.main.controller.packs.pokemon_pack_controller import api as pokemon_pack_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns

BASE_URL = '/api'

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Cabronis',
          version='0.1',
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
api.add_namespace(pokemon_pack_ns, path=BASE_URL + '/pokemon-pack')
api.add_namespace(basketball_pack_ns, path=BASE_URL + '/basketball-pack')

CORS(api.blueprint)
