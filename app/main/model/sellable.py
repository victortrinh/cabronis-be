from enum import Enum

from .. import db


class SellableTheme(Enum):
    pokemon = 'pokemon'
    basketball = 'basketball'
    football = 'football'
    baseball = 'baseball'
    hockey = 'hockey'


class Sellable(db.Model):
    __tablename__ = 'sellables'

    sellable_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image_path = db.Column(db.String(256))
    stock = db.Column(db.Integer)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    category = db.Column(db.String(64))
    team = db.Column(db.String(64))
    theme = db.Column(db.Enum(SellableTheme))
    type = db.Column(db.String(64))

    __mapper_args__ = {
        'polymorphic_identity': 'sellable',
        'polymorphic_on': type
    }


class Card(Sellable):
    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, db.ForeignKey('sellables.sellable_id'), primary_key=True)
    year = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'card'
    }

    def __repr__(self):
        return '<Card {}>'.format(self.name)


class Pack(Sellable):
    __tablename__ = 'packs'

    pack_id = db.Column(db.Integer, db.ForeignKey('sellables.sellable_id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'pack'
    }

    def __repr__(self):
        return '<Pack {}>'.format(self.name)


class Box(Sellable):
    __tablename__ = 'boxes'

    box_id = db.Column(db.Integer, db.ForeignKey('sellables.sellable_id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'box'
    }

    def __repr__(self):
        return '<Box {}>'.format(self.name)
