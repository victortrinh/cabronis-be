from .. import db


class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    sellable_id = db.Column(db.Integer, db.ForeignKey('sellables.sellable_id'), primary_key=True)
    date_added = db.Column(db.DateTime)
    sellable = db.relationship('Sellable')
