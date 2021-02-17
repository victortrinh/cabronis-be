from flask_restplus import Namespace, fields

from ..model.sellable import SellableTheme


class WishlistDTO:
    api = Namespace('Wishlist', description='Wishlist Operations')

    wishlist = api.model('Wishlist', {
        'name': fields.String(description='The wishlist item name'),
        'description': fields.String(description='The description of the wishlist item'),
        'image_path': fields.String(description='The image of the wishlist item'),
        'stock': fields.Integer(description='The amount of stocks for this wishlist item'),
        'price': fields.Float(description='The price of the wishlist item'),
        'category': fields.String(description='The category of the wishlist item'),
        'team': fields.String(description='The team of the wishlist item'),
        'theme': fields.String(description='The theme of the wishlist item',
                               enum=SellableTheme._member_names_),
        'type': fields.String(description='The type of the wishlist item'),
        'year': fields.String(description='The year associated with the wishlist item')
    })


class PackDTO:
    api = Namespace('Pack', description='Pack operations')

    pack = api.model('Pack', {
        'name': fields.String(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
        'stock': fields.Integer(required=True, description='The amount of stocks for this pack'),
        'price': fields.Float(required=True, description='The price of the pack'),
        'category': fields.String(required=False, description='The category of the pack'),
        'team': fields.String(required=False, description='The team of the pack'),
        'theme': fields.String(required=True, description='The theme of the pack', enum=SellableTheme._member_names_)
    })
