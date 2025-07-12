import boto3
import os
from concurrent.futures import ThreadPoolExecutor

def upload_file(s3_client, bucket_name, file_path):
    key = os.path.basename(file_path)
    s3_client.upload_file(Filename=file_path, Bucket=bucket_name, Key=key)

def batch_upload_files(s3_client, bucket_name, file_paths, max_threads=5):
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [
            executor.submit(upload_file, s3_client, bucket_name, file_path)
            for file_path in file_paths
        ]
        for future in futures:
            future.result()

if __name__ == "__main__":
    s3 = boto3.client('s3')
    bucket_name = "my-bucket"
    file_paths = ["example1.txt", "example2.txt", "example3.txt"]

    batch_upload_files(s3, bucket_name, file_paths)
