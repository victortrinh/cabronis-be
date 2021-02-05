from app.main import db
from app.main.model.sellable import PokemonPack


def get_packs():
    return PokemonPack.query.all()


def get_pack(pack_id):
    return PokemonPack.query.filter_by(id=pack_id).first()


def save_new_pack(data):
    new_pack = PokemonPack(
        name=data['name'],
        description=data['description'],
        image_str=data['image_str'],
        stock=data['stock'],
        price=data['price'],
        category=data['category']
    )
    save_changes(new_pack)
    response_object = {
        'id': new_pack.id,
    }
    return response_object, 201


def update_packs(data):
    query = db.session.query(PokemonPack)
    for pack in data:
        record = query.filter(PokemonPack.id == pack['id']).first()
        record.name = pack['name'],
        record.description = pack['description'],
        record.image_str = pack['image_str'],
        record.stock = pack['stock'],
        record.price = pack['price'],
        record.category = pack['category']
    db.session.flush()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated rows.',
    }
    return response_object, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_pack(data):
    pack = PokemonPack.query.filter_by(id=data['id']).one()
    db.session.delete(pack)
    db.session.commit()
    return {'message': "Pokemon Pack with id " + str(data['id']) + " was deleted successfully."}, 200
