from .. import db


class Sellable(db.Model):
    __abstract__ = True

    name = db.Column(db.String(64), unique=False)
    image_str = db.Column(db.String(256), unique=False)
    stock = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False)
    description = db.Column(db.Text, unique=False)


class Card(Sellable):
    __abstract__ = True


class Pack(Sellable):
    __abstract__ = True


class Box(Sellable):
    __abstract__ = True


class PokemonCard(Card):
    __tablename__ = "pokemon_cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return '<Pokemon Card {}>'.format(self.name)


class BasketballCard(Card):
    __tablename__ = "basketball_cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, unique=False)
    team = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return '<Basketball Card {}>'.format(self.name)


class PokemonPack(Pack):
    __tablename__ = "pokemon_packs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return '<Pokemon Pack {}>'.format(self.name)


class BasketballPack(Pack):
    __tablename__ = "basketball_packs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Basketball Pack {}>'.format(self.name)


class PokemonBox(Box):
    __tablename__ = "pokemon_boxes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return '<Pokemon Box {}>'.format(self.name)


class BasketballBox(Box):
    __tablename__ = "basketball_boxes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Basketball Box {}>'.format(self.name)
