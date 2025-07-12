import os
import boto3
from concurrent.futures import ThreadPoolExecutor

def download_object(s3_client, bucket_name, key, local_path):
    local_file_path = os.path.join(local_path, key)
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
    s3_client.download_file(Bucket=bucket_name, Key=key, Filename=local_file_path)

def download_files_from_s3(s3_client, bucket_name, local_path, max_threads=5):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    s3_keys = [obj['Key'] for obj in response.get('Contents', [])]

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
    local_path = "path/to/local/folder"

    download_files_from_s3(s3, bucket_name, local_path)