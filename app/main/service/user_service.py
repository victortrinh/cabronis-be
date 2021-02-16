import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()

    if user:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }

        return response_object, 409

    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password'],
        registered_on=datetime.datetime.utcnow()
    )

    db.session.add(new_user)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
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

    user.password = data["password"]
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
