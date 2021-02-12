from app.main import db
from app.main.model.sellable import Pack


def get_packs():
    return Pack.query.all()


def get_pack(pack_id):
    pack = Pack.query.filter_by(pack_id=pack_id).first()

    if not pack:
        response_object = {
            'status': 'fail',
            'message': 'Pack does not exist.'
        }
        return response_object, 409

    return pack


def save_new_pack(pack):
    new_pack = Pack(
        name=pack['name'],
        description=pack['description'],
        image_str=pack['image_str'],
        stock=pack['stock'],
        price=pack['price'],
        category=pack['category'],
        team=pack['team'],
        theme=pack['theme']
    )

    db.session.add(new_pack)
    db.session.commit()

    response_object = {
        'pack_id': new_pack.pack_id,
    }
    return response_object, 201


def update_pack(pack_id, pack):
    existing_pack = Pack.query.filter_by(pack_id=pack_id).first()

    if not existing_pack:
        response_object = {
            'status': 'fail',
            'message': 'Pack does not exist.'
        }
        return response_object, 409

    existing_pack.name = pack['name'],
    existing_pack.description = pack['description'],
    existing_pack.image_str = pack['image_str'],
    existing_pack.stock = pack['stock'],
    existing_pack.price = pack['price'],
    existing_pack.category = pack['category'],
    existing_pack.team = pack['team'],
    existing_pack.theme = pack['theme']

    db.session.flush()
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Successfully updated rows.',
    }
    return response_object, 201


def delete_pack(pack_id):
    existing_pack = Pack.query.filter_by(pack_id=pack_id).first()

    if not existing_pack:
        response_object = {
            'status': 'fail',
            'message': 'Pack does not exist.'
        }
        return response_object, 409

    db.session.delete(existing_pack)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': "Pack was deleted successfully."
    }
    return response_object, 200
