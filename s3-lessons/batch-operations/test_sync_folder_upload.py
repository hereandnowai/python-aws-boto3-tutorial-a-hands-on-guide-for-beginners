import os
import unittest
from moto import mock_s3
import boto3
import tempfile
import shutil

class TestSyncFolderToS3(unittest.TestCase):

    @mock_s3
    def test_sync_folder_to_s3(self):
        from sync_folder_upload import sync_folder_to_s3
        # Create an S3 client
        s3 = boto3.client('s3')

        # Create a mock bucket
        bucket_name = "test-bucket"
        s3.create_bucket(Bucket=bucket_name)

        # Create a temporary folder with sample files
        temp_folder = tempfile.mkdtemp()
        file_paths = []
        for i in range(3):
            file_name = f"example{i + 1}.txt"
            file_path = os.path.join(temp_folder, file_name)
            file_paths.append(file_path)
            with open(file_path, "w") as f:
                f.write(f"Content of {file_name}")

        # Synchronize the temporary folder to the S3 bucket
        sync_folder_to_s3(s3, bucket_name, temp_folder, max_threads=2)

        # Check if the files were uploaded correctly
        response = s3.list_objects_v2(Bucket=bucket_name)
        self.assertEqual(len(response['Contents']), 3)

        uploaded_keys = [obj['Key'] for obj in response['Contents']]
        expected_keys = [os.path.basename(file_path) for file_path in file_paths]
        self.assertListEqual(uploaded_keys, expected_keys)

        # Clean up the temporary folder
        shutil.rmtree(temp_folder)

if __name__ == "__main__":
    unittest.main()