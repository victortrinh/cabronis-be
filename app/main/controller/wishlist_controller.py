from flask_restplus import Resource

from ..dto.sellable_dto import WishlistDTO
from ..service.auth_service import Auth
from ..service.wishlist_service import add_to_wishlist, \
    remove_from_wishlist, get_wishlist

api = WishlistDTO.api
wishlist = WishlistDTO.wishlist

auth = Auth.auth_token


@api.route('/<user_id>')
@api.param('user_id', 'The user identifier')
@api.doc('get a user\'s wishlist')
class Get(Resource):
    @auth.login_required
    @api.doc('retrieve sellables from a user\'s wishlist')
    @api.marshal_with(wishlist)
    def get(self, user_id):
        return get_wishlist(user_id)


@api.route('/<user_id>/save/<sellable_id>')
@api.param('user_id', 'The user identifier')
@api.param('sellable_id', 'The sellable identifier')
class Add(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('add a sellable to a user\'s wishlist')
    def post(self, user_id, sellable_id):
        return add_to_wishlist(user_id, sellable_id)


@api.route('/<user_id>/delete/<sellable_id>')
@api.param('user_id', 'The user identifier')
@api.param('sellable_id', 'The sellable identifier')
class Delete(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('remove a sellable from a user\'s wishlist')
    def delete(self, user_id, sellable_id):
        return remove_from_wishlist(user_id, sellable_id)
