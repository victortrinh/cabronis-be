from enum import Enum

from .. import db


class SellableType(Enum):
    pokemon = "pokemon"
    basketball = "basketball"


class Sellable(db.Model):
    __abstract__ = True

    name = db.Column(db.String(64), unique=False)
    image_str = db.Column(db.String(256), unique=False)
    stock = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False)
    description = db.Column(db.Text, unique=False)
    category = db.Column(db.String(64), unique=False)
    year = db.Column(db.Integer, unique=False)
    team = db.Column(db.String(64), unique=False)
    type = db.Column(db.Enum(SellableType), unique=False)


class Card(Sellable):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Card {}>'.format(self.name)


class Pack(Sellable):
    __tablename__ = "packs"

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Pack {}>'.format(self.name)


class Box(Sellable):
    __tablename__ = "boxes"

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Box {}>'.format(self.name)
