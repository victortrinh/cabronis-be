import os
import cloudinary

from flask import current_app
from werkzeug.utils import secure_filename

cloudinary.config(
    cloud_name=current_app.config['CLOUDIFY_CLOUD_NAME'],
    api_key=current_app.config['CLOUDIFY_API_KEY'],
    api_secret=current_app.config['CLOUDIFY_API_SECRET']
)


def save_new_image(files):

    if 'file' not in files:
        response_object = {
            'status': 'fail',
            'message': 'No file provided.'
        }
        return response_object, 400

    file = files['file']
    file_name = file.filename

    if '.' not in file_name:
        response_object = {
            'status': 'fail',
            'message': 'File has no extension.'
        }
        return response_object, 400

    allowed_file_extensions = current_app.config['IMAGE_ALLOWED_EXTENSIONS']

    if file_name.split('.')[-1].lower() not in allowed_file_extensions:
        allowed_extensions_str = ' '.join(allowed_file_extensions)

        response_object = {
            'status': 'fail',
            'message': 'File extension is not supported. Extensions supported: ' + allowed_extensions_str + '.'
        }
        return response_object, 422

    file.seek(0, os.SEEK_END)
    file_length = file.tell()

    max_file_size_mb = current_app.config['IMAGE_MAX_FILE_SIZE']
    max_file_size_b = max_file_size_mb * 1024 ** 2

    if file_length > max_file_size_b:
        response_object = {
            'status': 'fail',
            'message': 'File size exceeds allowed size of ' + str(max_file_size_mb) + 'MB.'
        }
        return response_object, 422

    # file_name = secure_filename(file_name)
    # file_path = os.path.join(current_app.config['IMAGE_UPLOAD_DIRECTORY'], file_name)
    #
    # file.save(file_path)

    response = cloudinary.uploader.upload(file)

    # response_object = {
    #     'image_path': file_path,
    # }

    return response, 201
