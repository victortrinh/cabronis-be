from flask_restplus import Namespace, fields

from ..model.sellable import SellableTheme


class PackDTO:
    api = Namespace('Pack', description='Pack operations')

    pack = api.model('Pack', {
        'name': fields.String(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
        'image_str': fields.String(required=True, description='The image of the pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pack'),
        'price': fields.Float(required=True, description='The price of the pack'),
        'category': fields.String(required=False, description='The category of the pack'),
        'team': fields.String(required=False, description='The team of the pack'),
        'theme': fields.String(required=True, description='The theme of the pack', enum=SellableTheme.member_names_)
    })
