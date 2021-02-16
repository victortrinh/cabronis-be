from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('User', description='user related operations')

    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'password': fields.String(required=True, description='user password')
    })

    user_change_password = api.model('user_change_password', {
        'email': fields.String(required=True, description='user email address'),
        'current_password': fields.String(required=True, description='Current user password'),
        'password': fields.String(required=True, description='New user password'),
        'confirm_password': fields.String(required=True, description='New user confirm password'),
    })
