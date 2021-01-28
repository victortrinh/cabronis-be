from flask_restplus import Namespace, fields


class PackDTO:
    api = Namespace('Pack', description='Pack operations')
    pack = api.model('Pack', {
        'name': fields.String(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
    })
    full_pack = api.model('Pack with id', {
        'id': fields.Integer(required=True, description='The pack identifier'),
        'name': fields.Integer(required=True, description='The pack name'),
        'description': fields.String(required=True, description='The description of the pack'),
    })
    pack_id = api.model('Pack id', {
        'id': fields.Integer(required=True, description='The pack identifier'),
    })
