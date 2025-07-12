import os
import unittest
import boto3
from moto import mock_s3

@mock_s3
class TestS3Upload(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        # Create a test bucket
        self.s3_resource.create_bucket(Bucket='test-bucket')

    def test_upload_file_to_s3(self):
        from upload_file import upload_file_to_s3

        # Upload a test file to the test bucket
        file_name = 'test_file.txt'
        with open(file_name, 'w') as f:
            f.write('Test file contents')

        result = upload_file_to_s3(file_name, 'test-bucket', object_name='test_file.txt')

        # Verify that the file was uploaded successfully
        bucket = self.s3_resource.Bucket('test-bucket')
        objs = list(bucket.objects.filter(Prefix='test_file.txt'))
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].key, 'test_file.txt')
        self.assertEqual(result, True)

        # Delete test file
        os.unlink(file_name)

    def test_upload_generated_file_object_to_s3(self):
        from upload_file import upload_generated_file_object_to_s3

        result = upload_generated_file_object_to_s3('test-bucket', object_name='test_file.txt')

        # Verify that the file was uploaded successfully
        bucket = self.s3_resource.Bucket('test-bucket')
        objs = list(bucket.objects.filter(Prefix='test_file.txt'))
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].key, 'test_file.txt')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
