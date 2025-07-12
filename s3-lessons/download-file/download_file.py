from io import BytesIO
import boto3

S3_CLIENT = boto3.client('s3')
local_file_path = 'local-file.txt'

def download_callback(bytes_amount):
    print(f'Downloaded {bytes_amount} bytes')

def download_file(bucket_name, object_key, local_file_path):
    S3_CLIENT.download_file(
        bucket_name,
        object_key,
        local_file_path,
        Callback=download_callback
    )

def download_file_to_memory(bucket_name, object_key):
    f = BytesIO()
    S3_CLIENT.download_fileobj(bucket_name, object_key, f)
    return f.getvalue()
