import datetime

from app.main import db
from app.main.model.sellable import Sellable
from app.main.model.user import User, wishlist_table


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


def get_wishlist(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    wishlist = db.session.query(wishlist_table).filter_by(user=user_id).all()

    return wishlist


def add_to_wishlist(user_id, sellable_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    sellable = Sellable.query.filter_by(sellable_id=sellable_id).first()

    if not sellable:
        response_object = {
            'status': 'fail',
            'message': 'Sellable does not exist.'
        }

        return response_object, 404

    if User.query.join(wishlist_table).join(Sellable).filter((wishlist_table.c.user == user_id) &
                                                             (wishlist_table.c.sellable == sellable_id)).first():
        response_object = {
            'status': 'fail',
            'message': 'Sellable already in wishlist.'
        }

        return response_object, 409

    user.wishlist.append(sellable)

    db.session.add(user)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully added sellable to wishlist.'
    }

    return response_object, 201


def remove_from_wishlist(user_id, sellable_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    sellable = Sellable.query.filter_by(sellable_id=sellable_id).first()

    if not sellable:
        response_object = {
            'status': 'fail',
            'message': 'Sellable does not exist.'
        }

        return response_object, 404

    if not User.query.join(wishlist_table).join(Sellable).filter((wishlist_table.c.user == user_id) &
                                                                 (wishlist_table.c.sellable == sellable_id)).first():
        response_object = {
            'status': 'fail',
            'message': 'Sellable not in wishlist.'
        }

        return response_object, 409

    user.wishlist.remove(sellable)

    db.session.add(user)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully removed sellable from wishlist.'
    }

    return response_object, 201
