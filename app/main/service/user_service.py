import datetime
import re

from app.main import db
from app.main.model.user import User, UserRole
from app.main.service.auth_service import Auth


def check_password(password):
    SpecialSym = ['$', '@', '#', '%', '!']

    if len(password) < 8:
        return 'Password length should be at least 8.'

    if len(password) > 20:
        return 'Password length should be not be greater than 8.'

    if not any(char.isdigit() for char in password):
        return 'Password should have at least one numeral.'

    if not any(char.isupper() for char in password):
        return 'Password should have at least one uppercase letter.'

    if not any(char.islower() for char in password):
        return 'Password should have at least one lowercase letter.'

    if not any(char in SpecialSym for char in password):
        return 'Password should have at least one of the symbols $, @, #, % or !.'

    return None


def check_email(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    if not EMAIL_REGEX.match(email):
        return 'Please enter a valid email address. (example@mail.com).'

    return None


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()

    if user:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }

        return response_object, 409

    passwordMessage = check_password(data['password'])

    if passwordMessage:
        response_object = {
            'status': 'fail',
            'message': passwordMessage
        }

        return response_object, 409

    emailMessage = check_email(data['email'])

    if emailMessage:
        response_object = {
            'status': 'fail',
            'message': emailMessage
        }

        return response_object, 409

    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password'],
        roles=['buyer'],
        registered_on=datetime.datetime.utcnow()
    )

    db.session.add(new_user)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }

    return response_object, 201


def update_user(user_id, user):
    existing_user = User.query.filter_by(user_id=user_id).first()

    if not existing_user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }
        return response_object, 409

    emailMessage = check_email(user['email'])

    if emailMessage:
        response_object = {
            'status': 'fail',
            'message': emailMessage
        }

        return response_object, 409

    existing_user.first_name = user['first_name'],
    existing_user.last_name = user['last_name'],
    existing_user.email = user['email'],
    existing_user.roles = user['roles']

    db.session.flush()
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully updated user.',
    }
    return response_object, 201


def change_user_password(data):
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    if not user.check_password(data['current_password']):
        response_object = {
            'status': 'fail',
            'message': 'Current password is wrong.'
        }

        return response_object, 409

    if data['password'] != data['confirm_password']:
        response_object = {
            'status': 'fail',
            'message': 'Passwords do not match.'
        }

        return response_object, 409

    user.password = data['password']
    db.session.flush()
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully changed password.'
    }

    return response_object, 201


def get_all_users():
    return User.query.all()


def get_a_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    return user


def get_roles(data):
    if data:
        auth_token = data.split(' ')[1]
        resp = User.decode_auth_token(auth_token)

        if not isinstance(resp, str):
            user = User.query.filter_by(user_id=resp).first()
            return user
        else:
            return []
    else:
        return []
