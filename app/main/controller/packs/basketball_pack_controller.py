from flask import request
from flask_restplus import Resource

from app.main.dto.sellable_dto import BasketballPackDTO
from app.main.service.auth_service import Auth
from app.main.service.packs.basketball_pack_service import get_pack, get_packs, save_new_pack, delete_pack, update_packs

api = BasketballPackDTO.api
pack = BasketballPackDTO.pack
auth = Auth.auth_token


@api.route('/all')
class GetPacks(Resource):
    @api.doc('Get all basketball packs')
    @api.marshal_with(pack)
    def get(self):
        return get_packs()


@api.route('/<pack_id>')
@api.param('pack_id', 'The Basketball Pack identifier')
@api.response(404, 'Basketball Pack not found.')
class GetPack(Resource):
    @api.doc('Get basketball pack by identifier')
    @api.marshal_with(pack)
    def get(self, pack_id):
        pack = get_pack(pack_id)
        if not pack:
            api.abort(404)
        else:
            return pack


@api.route('/save')
class SavePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Save new basketball pack')
    @api.expect(BasketballPackDTO.pack, validate=True)
    def post(self):
        data = request.json
        return save_new_pack(data)


@api.route('/update')
class UpdatePacks(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Update a basketball pack')
    @api.expect([BasketballPackDTO.full_pack], validate=True)
    def put(self):
        data = request.json
        return update_packs(data)


@api.route('/delete')
class DeletePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Delete a basketball pack')
    @api.expect(BasketballPackDTO.pack_id, validate=True)
    def delete(self):
        data = request.json
        return delete_pack(data)
