from flask_restplus import Namespace, fields

from ..model.user import UserRole


class UserDto:
    api = Namespace('User', description='user related operations')

    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'password': fields.String(required=True, description='user password')
    })

    user_roles = api.model('user', {
        'roles': fields.List(fields.String(required=False, description='user roles', enum=UserRole._member_names_)),
    })

    user_with_roles = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'password': fields.String(required=True, description='user password'),
        'roles': fields.List(fields.String(required=False, description='user roles', enum=UserRole._member_names_)),
    })

    user_change_password = api.model('user_change_password', {
        'email': fields.String(required=True, description='user email address'),
        'current_password': fields.String(required=True, description='Current user password'),
        'password': fields.String(required=True, description='New user password'),
        'confirm_password': fields.String(required=True, description='New user confirm password'),
    })
