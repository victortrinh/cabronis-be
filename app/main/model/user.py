import datetime
from enum import Enum

import jwt

from app.main.model.blacklist import BlacklistToken
from .. import db, flask_bcrypt
from ..config import key


class UserRole(Enum):
    admin = 'admin'
    seller = 'seller'
    buyer = 'buyer'


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=False)
    last_name = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    roles = db.Column(db.ARRAY(db.String(120)))
    password_hash = db.Column(db.String(128))
    sellables = db.relationship('Wishlist')

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @staticmethod
    def is_valid_token(auth_token):
        try:
            payload = jwt.decode(auth_token, key)
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError:
            return False
