from app.main import db
from app.main.model.sellable import Pack


def get_packs():
    return Pack.query.all()


def get_pack(pack_id):
    return Pack.query.filter_by(id=pack_id).first()


def save_new_pack(data):
    new_pack = Pack(
        name=data['name'],
        description=data['description'],
        image_str=data['image_str'],
        stock=data['stock'],
        price=data['price'],
        category=data['category'],
        year=data['year'],
        team=data['team'],
        type=data['type']
    )
    db.session.add(data)
    db.session.commit()
    response_object = {
        'id': new_pack.id,
    }
    return response_object, 201


def update_packs(data):
    query = db.session.query(Pack)
    for pack in data:
        record = query.filter(Pack.id == pack['id']).first()

        if not record:
            response_object = {
                'status': 'fail',
                'message': 'Pack with id ' + str(pack['id']) + ' does not exist.'
            }
            return response_object, 409

        record.name = pack['name'],
        record.description = pack['description'],
        record.image_str = pack['image_str'],
        record.stock = pack['stock'],
        record.price = pack['price'],
        record.category = pack['category'],
        record.year = pack['year'],
        record.team = pack['team'],
        record.type = pack['type']

    db.session.flush()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated rows.',
    }
    return response_object, 201


def delete_pack(data):
    pack = Pack.query.filter_by(id=data['id']).first()

    if not pack:
        response_object = {
            'status': 'fail',
            'message': 'Pack with id ' + str(data['id']) + ' does not exist.'
        }
        return response_object, 409

    db.session.delete(pack)
    db.session.commit()
    return {'message': "Pack with id " + str(data['id']) + " was deleted successfully."}, 200
