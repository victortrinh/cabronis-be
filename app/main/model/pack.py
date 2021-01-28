from .. import db


class Pack(db.Model):
    __tablename__ = "packs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    description = db.Column(db.Text(), unique=False)

    def __repr__(self):
        return '<Pack {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
