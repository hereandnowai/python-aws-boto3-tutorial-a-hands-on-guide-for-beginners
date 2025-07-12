import unittest
from moto import mock_s3
import boto3
import tempfile
import shutil
import os
from download_files import download_files_from_s3

class TestDownloadFilesFromS3(unittest.TestCase):

    @mock_s3
    def test_download_files_from_s3(self):
        # Create an S3 client
        s3 = boto3.client('s3')

        # Create a mock bucket
        bucket_name = "test-bucket"
        s3.create_bucket(Bucket=bucket_name)

        # Upload sample files to the mock bucket
        sample_files = {}
        for i in range(3):
            file_name = f"example{i + 1}.txt"
            sample_files[file_name] = f"Content of {file_name}"
            s3.put_object(Bucket=bucket_name, Key=file_name, Body=sample_files[file_name])

        # Create a temporary folder to download files
        temp_folder = tempfile.mkdtemp()

        # Download files from the S3 bucket
        download_files_from_s3(s3, bucket_name, temp_folder)

        # Check if the files were downloaded correctly
        for file_name, content in sample_files.items():
            with open(os.path.join(temp_folder, file_name), "r") as f:
                self.assertEqual(f.read(), content)

        # Clean up the temporary folder
        shutil.rmtree(temp_folder)

if __name__ == "__main__":
    unittest.main()