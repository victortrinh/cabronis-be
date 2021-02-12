from flask import request
from flask_restplus import Resource

from app.main.dto.sellable_dto import PackDTO
from app.main.service.auth_service import Auth
from app.main.service.pack_service import get_pack, get_packs, save_new_pack, update_pack, delete_pack

api = PackDTO.api
pack = PackDTO.pack
auth = Auth.auth_token


@api.route('/all')
class GetPacks(Resource):
    @api.doc('Get all packs')
    @api.marshal_with(pack)
    def get(self):
        return get_packs()


@api.route('/<pack_id>')
@api.param('pack_id', 'The Pack identifier')
@api.response(404, 'Pack not found.')
class GetPack(Resource):
    @api.doc('Get pack by identifier')
    @api.marshal_with(pack)
    def get(self, pack_id):
        return get_pack(pack_id)


@api.route('/save')
class SavePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Save new pack')
    @api.expect(PackDTO.pack, validate=True)
    def post(self):
        data = request.json
        return save_new_pack(data)


@api.route('/update/<pack_id>')
@api.param('pack_id', 'The Pack identifier')
class UpdatePacks(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Update a pack')
    @api.expect(PackDTO.pack, validate=True)
    def put(self, pack_id):
        data = request.json
        return update_pack(pack_id, data)


@api.route('/delete/<pack_id>')
@api.param('pack_id', 'The Pack identifier')
class DeletePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Delete a pack')
    def delete(self, pack_id):
        return delete_pack(pack_id)
