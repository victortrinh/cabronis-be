from flask_restplus import Resource
from flask import request
from ..service.pack_service import get_packs, save_new_pack, delete_pack, update_packs
from ..dto.pack_dto import PackDTO
from ..service.auth_service import Auth
from flask_httpauth import HTTPTokenAuth

api = PackDTO.api
auth = Auth.auth


@api.route('/all')
class GetPacks(Resource):
    @api.doc('Get all packs')
    def get(self):
        return get_packs()


@api.route('/save')
class SavePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Save new pack')
    @api.expect(PackDTO.pack, validate=True)
    def post(self):
        data = request.json
        return save_new_pack(data)


@api.route('/update')
class UpdatePacks(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Update a pack')
    @api.expect([PackDTO.full_pack], validate=True)
    def put(self):
        data = request.json
        return update_packs(data)


@api.route('/delete')
class DeletePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Delete a pack')
    @api.expect(PackDTO.pack_id, validate=True)
    def delete(self):
        data = request.json
        return delete_pack(data)
