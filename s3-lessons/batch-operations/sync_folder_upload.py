import os
import hashlib
import boto3
from concurrent.futures import ThreadPoolExecutor
from upload_files import batch_upload_files

def get_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_s3_objects(s3_client, bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    return {obj['Key']: obj['ETag'].strip('"') for obj in response.get('Contents', [])}

def sync_folder_to_s3(s3_client, bucket_name, folder_path, max_threads=5):
    local_files = {
        os.path.join(root, file): get_md5(os.path.join(root, file))
        for root, _, files in os.walk(folder_path)
        for file in files
    }
    s3_objects = get_s3_objects(s3_client, bucket_name)

    files_to_upload = [
        file_path
        for file_path, md5 in local_files.items()
        if os.path.basename(file_path) not in s3_objects or md5 != s3_objects[os.path.basename(file_path)]
    ]

    batch_upload_files(s3_client, bucket_name, files_to_upload, max_threads=max_threads)

if __name__ == "__main__":
    s3 = boto3.client('s3')
    bucket_name = "my-bucket"
    folder_path = "path/to/your/folder"

    sync_folder_to_s3(s3, bucket_name, folder_path, max_threads=5)