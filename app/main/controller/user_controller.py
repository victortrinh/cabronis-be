from flask import request
from flask_restplus import Resource

from ..dto.user_dto import UserDto
from ..service.auth_service import Auth
from ..service.user_service import save_new_user, get_all_users, get_a_user, change_user_password, get_roles

api = UserDto.api
user = UserDto.user
user_roles = UserDto.user_roles
user_with_roles = UserDto.user_with_roles
user_change_password = UserDto.user_change_password

auth = Auth.auth_token


@api.route('/')
class UserList(Resource):
    @auth.login_required(role=['admin', 'seller'])
    @api.doc(security='Bearer')
    @api.doc('list of registered users')
    @api.marshal_list_with(user_with_roles, envelope='data')
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
    @auth.login_required(role=['admin', 'seller'])
    @api.doc(security='Bearer')
    @api.doc('get a user')
    @api.response(404, 'User not found.')
    @api.marshal_with(user)
    def get(self, user_id):
        return get_a_user(user_id)


@api.route('/roles')
class GetRoles(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Get role')
    @api.marshal_with(user_roles)
    def post(self):
        auth_header = request.headers.get('Authorization')
        return get_roles(data=auth_header)
