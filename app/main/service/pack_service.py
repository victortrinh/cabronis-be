# import uuid
# import datetime

from app.main import db
from app.main.model.pack import Pack


def get_packs():
    return Pack.query.all()


def get_pack(pack_id):
    return Pack.query.filter_by(id=pack_id).first()


def save_new_pack(data):
    new_pack = Pack(
        name=data['name'],
        description=data['description']
    )
    save_changes(new_pack)
    response_object = {
        'id': new_pack.id,
    }
    return response_object, 201


def update_packs(data):
    query = db.session.query(Pack)
    for pack in data:
        new_query = query.filter(Pack.id == pack['id'])
        record = new_query.one()
        record.name = pack["name"]
        record.description = pack["description"]
    db.session.flush()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated row.',
    }
    return response_object, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_pack(data):
    pack = Pack.query.filter_by(id=data['id']).one()
    db.session.delete(pack)
    db.session.commit()
    return {'message': "Pack id : " + str(data['id']) + " was deleted successfully"}, 200
