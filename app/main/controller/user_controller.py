from flask import request
from flask_restplus import Resource

from ..dto.user_dto import UserDto
from ..service.auth_service import Auth
from ..service.user_service import save_new_user, get_all_users, get_a_user, change_user_password

api = UserDto.api
user = UserDto.user
user_change_password = UserDto.user_change_password

auth = Auth.auth_token


@api.route('/')
class UserList(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(user, envelope='data')
    def get(self):
        """List all registered users"""
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
    @api.response(201, 'User successfully changed password.')
    @api.doc('Change user password')
    @api.expect(user_change_password, validate=True)
    def post(self):
        """Changes user password"""
        data = request.json
        return change_user_password(data=data)


@api.route('/<id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('get a user')
    @api.marshal_with(user)
    def get(self, public_id):
        """Get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
