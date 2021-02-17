from flask import request
from flask_restplus import Namespace, Resource
from werkzeug.datastructures import FileStorage

from app.main.service.auth_service import Auth
from app.main.service.image_service import save_new_image

api = Namespace('Image', description='Image operations')
auth = Auth.auth_token

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@api.route('/save')
@api.expect(upload_parser)
class SaveImage(Resource):
    @auth.login_required
    @api.doc(security='Bearer')
    @api.doc('Save new image')
    def post(self):
        files = request.files
        return save_new_image(files)
