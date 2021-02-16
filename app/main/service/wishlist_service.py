from datetime import datetime

from app.main import db
from app.main.model.sellable import Sellable
from app.main.model.user import User
from app.main.model.wishlist import Wishlist


def get_wishlist(user_id):
    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        response_object = {
            'status': 'fail',
            'message': 'User does not exist.'
        }

        return response_object, 404

    wishlist = db.session.query(Sellable).join(Wishlist).filter(Wishlist.user_id == user_id).all()

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

    if Wishlist.query.filter_by(user_id=user_id, sellable_id=sellable_id).first():
        response_object = {
            'status': 'fail',
            'message': 'Sellable already in wishlist.'
        }

        return response_object, 409

    wishlist_item = Wishlist(date_added=datetime.now())
    wishlist_item.sellable = sellable
    user.sellables.append(wishlist_item)

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

    wishlist_item = Wishlist.query.filter_by(user_id=user_id, sellable_id=sellable_id).first()

    if not wishlist_item:
        response_object = {
            'status': 'fail',
            'message': 'Sellable not in wishlist.'
        }

        return response_object, 409

    user.sellables.remove(wishlist_item)

    db.session.delete(wishlist_item)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully removed sellable from wishlist.'
    }

    return response_object, 201
