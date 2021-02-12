from flask import request
from flask_restplus import Resource

from ..dto.user_dto import UserDto
from ..service.auth_service import Auth
from ..service.user_service import save_new_user, get_all_users, get_a_user, change_user_password, add_to_wishlist, \
    remove_from_wishlist, get_wishlist

api = UserDto.api
user = UserDto.user
user_change_password = UserDto.user_change_password

auth = Auth.auth_token


@api.route('/')
class UserList(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('list of registered users')
    @api.marshal_list_with(user, envelope='data')
    def get(self):
        return get_all_users()


@api.route('/register')
class Register(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/changePassword')
class ChangePassword(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('change user password')
    @api.response(201, 'User successfully changed password.')
    @api.response(404, 'User not found.')
    @api.response(409, 'Incorrect password.')
    @api.expect(user_change_password, validate=True)
    def post(self):
        data = request.json
        return change_user_password(data=data)


@api.route('/<user_id>')
@api.param('user_id', 'The User identifier')
class User(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('get a user')
    @api.response(404, 'User not found.')
    @api.marshal_with(user)
    def get(self, user_id):
        return get_a_user(user_id)


@api.route('/<user_id>/wishlist')
@api.param('user_id', 'The user identifier')
@api.doc('get a user\'s wishlist')
class WishlistGet(Resource):
    @auth.login_required
    @api.doc('retrieve sellable IDs from a user\'s wishlist')
    def get(self, user_id):
        return get_wishlist(user_id)


@api.route('/<user_id>/wishlist/save/<sellable_id>')
@api.param('user_id', 'The user identifier')
@api.param('sellable_id', 'The sellable identifier')
class WishlistAdd(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('add a sellable to a user\'s wishlist')
    def post(self, user_id, sellable_id):
        return add_to_wishlist(user_id, sellable_id)


@api.route('/<user_id>/wishlist/delete/<sellable_id>')
@api.param('user_id', 'The user identifier')
@api.param('sellable_id', 'The sellable identifier')
class WishlistRemove(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('remove a sellable from a user\'s wishlist')
    def delete(self, user_id, sellable_id):
        return remove_from_wishlist(user_id, sellable_id)
