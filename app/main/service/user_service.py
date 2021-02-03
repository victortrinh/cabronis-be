import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def change_user_password(data):
    query = db.session.query(User)
    user = query.filter_by(email=data['email']).first()
    if not user.check_password(data['current_password']):
        response_object = {
            'status': 'fail',
            'message': 'Current password is wrong',
        }
        return response_object, 409

    if data['password'] != data['confirm_password']:
        response_object = {
            'status': 'fail',
            'message': 'Passwords do not match',
        }
        return response_object, 409

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'Users do not exists',
        }
        return response_object, 409

    user.password = data["password"]
    db.session.flush()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully changed password',
    }
    return response_object, 201


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
