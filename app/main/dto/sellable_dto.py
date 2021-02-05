from flask_restplus import Namespace, fields


class PokemonPackDTO:
    api = Namespace('PokemonPack', description='Pokemon Pack operations')

    pack = api.model('Pokemon Pack', {
        'name': fields.String(required=True, description='The pokemon pack name'),
        'description': fields.String(required=True, description='The description of the pokemon pack'),
        'image_str': fields.String(required=True, description='The image of the pokemon pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pokemon pack'),
        'price': fields.Float(required=True, description='The price of the pokemon pack'),
        'category': fields.String(required=True, description='The category of the pokemon pack')
    })
    full_pack = api.model('Pokemon Pack with id', {
        'id': fields.Integer(required=True, description='The pokemon pack identifier'),
        'name': fields.String(required=True, description='The pokemon pack name'),
        'description': fields.String(required=True, description='The description of the pokemon pack'),
        'image_str': fields.String(required=True, description='The image of the pokemon pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pokemon pack'),
        'price': fields.Float(required=True, description='The price of the pokemon pack'),
        'category': fields.String(required=True, description='The category of the pokemon pack')
    })
    pack_id = api.model('Pokemon Pack id', {
        'id': fields.Integer(required=True, description='The pokemon pack identifier'),
    })


class BasketballPackDTO:
    api = Namespace('BasketballPack', description='Basketball Pack operations')

    pack = api.model('Basketball Pack', {
        'name': fields.String(required=True, description='The basketball pack name'),
        'description': fields.String(required=True, description='The description of the basketball pack'),
        'image_str': fields.String(required=True, description='The image of the basketball pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this basketball pack'),
        'price': fields.Float(required=True, description='The price of the basketball pack'),
        'year': fields.Integer(required=True, description='The year of the basketball pack')
    })
    full_pack = api.model('Basketball Pack with id', {
        'id': fields.Integer(required=True, description='The basketball pack identifier'),
        'name': fields.String(required=True, description='The basketball pack name'),
        'description': fields.String(required=True, description='The description of the basketball pack'),
        'image_str': fields.String(required=True, description='The image of the basketball pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this basketball pack'),
        'price': fields.Float(required=True, description='The price of the basketball pack'),
        'year': fields.Integer(required=True, description='The year of the basketball pack')
    })
    pack_id = api.model('Basketball Pack id', {
        'id': fields.Integer(required=True, description='The basketball pack identifier'),
    })
