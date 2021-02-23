import logging

from flask import current_app
from flask_httpauth import HTTPTokenAuth

from ..model.user import User
from ..service.blacklist_service import save_token


class Auth:
    auth_token = HTTPTokenAuth(scheme='Bearer')

    @staticmethod
    @auth_token.verify_token
    def verify_token(token):
        if current_app.config.get('DISABLE_AUTHENTICATION', False):
            logging.warning(
                'Authentication is disabled. Skipped token validation.')
            return True
        if User.is_valid_token(token):
            return True
        return False

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user:
                if user.check_password(data.get('password')):
                    auth_token = User.encode_auth_token(user.user_id)
                    if auth_token:
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'email': user.email,
                            'roles': user.roles,
                            'Authorization': auth_token.decode()
                        }
                        return response_object, 200
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'The email address and password does not match our records.'
                    }
                    return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'The email address entered does not match any account. Please double check and try again. If not, create an account!'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(' ')[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(user_id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.blacklist_id,
                        'email': user.email,
                        'roles': user.roles,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    @auth_token.get_user_roles
    def get_user_roles(data):
        if current_app.config.get('DISABLE_AUTHENTICATION', False):
            logging.warning(
                'Authentication is disabled. Skipped token validation.')
            return ['buyer', 'seller', 'admin']

        auth_token = data["token"]
        resp = User.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            user = User.query.filter_by(user_id=resp).first()
            return user.roles
        else:
            return []
