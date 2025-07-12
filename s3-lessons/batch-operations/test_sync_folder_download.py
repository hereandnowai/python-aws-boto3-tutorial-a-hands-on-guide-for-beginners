import unittest
from moto import mock_s3
import boto3
import tempfile
import shutil
import os

class TestSyncS3BucketToLocalFolder(unittest.TestCase):

    @mock_s3
    def test_sync_s3_bucket_to_local_folder(self):
        from sync_folder_download import sync_s3_bucket_to_local_folder
        # Create an S3 client
        s3 = boto3.client('s3')

        # Create a mock bucket
        bucket_name = "test-bucket"
        s3.create_bucket(Bucket=bucket_name)

        # Upload sample files to the mock bucket with key prefix
        key_prefix = "sample_data/"
        sample_files = {}
        for i in range(3):
            file_name = f"example{i + 1}.txt"
            key = f"{key_prefix}{file_name}"
            sample_files[key] = f"Content of {file_name}"
            s3.put_object(Bucket=bucket_name, Key=key, Body=sample_files[key])

        # Create a temporary folder to download files
        temp_folder = tempfile.mkdtemp()

        # Synchronize S3 bucket content by key path to the temporary folder
        sync_s3_bucket_to_local_folder(s3, bucket_name, key_prefix, temp_folder)

        # Check if the files were downloaded correctly
        for key, content in sample_files.items():
            local_file_path = os.path.join(temp_folder, key)
            with open(local_file_path, "r") as f:
                self.assertEqual(f.read(), content)

        # Clean up the temporary folder
        shutil.rmtree(temp_folder)

if __name__ == "__main__":
    unittest.main()
