#import uuid
#import datetime

from flask import jsonify
from app.main import db
from app.main.model.pack import Pack


def get_packs():
    packs = Pack.query.all()
    return jsonify(packs=[pack.serialize() for pack in packs])


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
        record.name = assembly["name"]
        record.description = assembly["description"]
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
