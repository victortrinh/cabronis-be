from flask_restplus import Namespace, fields

from ..model.sellable import SellableType


class PackDTO:
    api = Namespace('Pack', description='Pack operations')

    pack = api.model('Pack', {
        'name': fields.String(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
        'image_str': fields.String(required=True, description='The image of the pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pack'),
        'price': fields.Float(required=True, description='The price of the pack'),
        'category': fields.String(required=False, description='The category of the pack'),
        'year': fields.Integer(required=False, description='The year of the pack'),
        'team': fields.String(required=False, description='The team of the pack'),
        'type': fields.String(required=True, description='The type of the pack', enum=SellableType.member_names_)

    })
    full_pack = api.model('Pack with id', {
        'id': fields.Integer(required=True, description='The pack identifier'),
        'name': fields.String(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
        'image_str': fields.String(required=True, description='The image of the pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pack'),
        'price': fields.Float(required=True, description='The price of the pack'),
        'category': fields.String(required=False, description='The category of the pack'),
        'year': fields.Integer(required=False, description='The year of the pack'),
        'team': fields.String(required=False, description='The team of the pack'),
        'type': fields.String(required=True, description='The type of the pack', enum=SellableType.member_names_)
    })
    pack_id = api.model('Pack id', {
        'id': fields.Integer(required=True, description='The pack identifier'),
    })
