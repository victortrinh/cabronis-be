import os

import boto3
from botocore.exceptions import ClientError
from flask import current_app


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

    s3_client = boto3.client('s3',
                             aws_access_key_id=current_app.config['BUCKETEER_ACCESS_KEY_ID'],
                             aws_secret_access_key=current_app.config['BUCKETEER_SECRET_ACCESS_KEY'])

    file_path = current_app.config['BUCKETEER_PREFIX_NAME'] + file_name

    try:
        s3_client.upload_fileobj(file, current_app.config['BUCKETEER_BUCKET_NAME'], file_path)
    except ClientError as e:
        response_object = {
            'status': 'fail',
            'message': 'Unable to upload file.'
        }
        return response_object, 422

    response_object = {
        'status': 'success',
        'message': 'File uploaded successfully under ' + file_path + '.'
    }

    return response_object, 201
