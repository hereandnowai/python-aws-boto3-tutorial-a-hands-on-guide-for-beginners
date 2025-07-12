import os
import boto3
from concurrent.futures import ThreadPoolExecutor

def download_object(s3_client, bucket_name, key, local_path):
    local_file_path = os.path.join(local_path, key)
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
    s3_client.download_file(Bucket=bucket_name, Key=key, Filename=local_file_path)

def sync_s3_bucket_to_local_folder(s3_client, bucket_name, key_prefix, local_path, max_threads=5):
    paginator = s3_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=key_prefix)

    s3_keys = []
    for page in page_iterator:
        s3_keys.extend([obj['Key'] for obj in page.get('Contents', [])])

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(download_object, s3_client, bucket_name, key, local_path)
            for key in s3_keys
        ]
        for future in futures:
            future.result()

if __name__ == "__main__":
    s3 = boto3.client('s3')
    bucket_name = "my-bucket"
    key_prefix = "path/to/key/prefix"
    local_path = "path/to/local/folder"

    sync_s3_bucket_to_local_folder(s3, bucket_name, key_prefix, local_path)
