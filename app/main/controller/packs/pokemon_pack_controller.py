from flask import request
from flask_restplus import Resource

from app.main.dto.sellable_dto import PokemonPackDTO
from app.main.service.auth_service import Auth
from app.main.service.packs.pokemon_pack_service import get_pack, get_packs, save_new_pack, delete_pack, update_packs

api = PokemonPackDTO.api
pack = PokemonPackDTO.pack
auth = Auth.auth_token


@api.route('/all')
class GetPacks(Resource):
    @api.doc('Get all pokemon packs')
    @api.marshal_with(pack)
    def get(self):
        return get_packs()


@api.route('/<pack_id>')
@api.param('pack_id', 'The Pokemon Pack identifier')
@api.response(404, 'Pokemon Pack not found.')
class GetPack(Resource):
    @api.doc('Get pokemon pack by identifier')
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
    @api.doc('Save new pokemon pack')
    @api.expect(PokemonPackDTO.pack, validate=True)
    def post(self):
        data = request.json
        return save_new_pack(data)


@api.route('/update')
class UpdatePacks(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Update a pokemon pack')
    @api.expect([PokemonPackDTO.full_pack], validate=True)
    def put(self):
        data = request.json
        return update_packs(data)


@api.route('/delete')
class DeletePack(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Delete a pokemon pack')
    @api.expect(PokemonPackDTO.pack_id, validate=True)
    def delete(self):
        data = request.json
        return delete_pack(data)
