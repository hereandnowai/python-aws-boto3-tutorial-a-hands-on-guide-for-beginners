from io import StringIO
import boto3
import moto
import os
import unittest
from unittest.mock import patch


@moto.mock_s3
class TestDownloadFileFromS3(unittest.TestCase):
    def setUp(self):
        # Set up a mock S3 bucket and file
        self.bucket_name = 'test-bucket'
        self.object_key = 'test-file.txt'

        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=self.bucket_name)
        self.s3_resource.Object(self.bucket_name, self.object_key).put(Body=b'test data')

    def test_download_file_from_s3(self):
        from download_file import download_file
        local_file_path = 'test-file.txt'

        # Call the download function
        with patch('sys.stdout', new = StringIO()) as print_output:
            expected_output = "Downloaded 9 bytes\n"
            download_file(self.bucket_name, self.object_key, local_file_path)
            self.assertEqual(print_output.getvalue(), expected_output)

        # Check that the file was downloaded successfully
        self.assertTrue(os.path.isfile(local_file_path))
        with open(local_file_path, 'rb') as f:
            self.assertEqual(f.read(), b'test data')

        os.unlink(local_file_path)

    def test_download_file_in_memory_from_s3(self):
        from download_file import download_file_to_memory

        # Call the download function
        file_content = download_file_to_memory(self.bucket_name, self.object_key)

        # Check that the file was downloaded successfully
        self.assertTrue(not file_content is None)
        self.assertEqual(file_content, b'test data')


if __name__ == '__main__':
    unittest.main()
