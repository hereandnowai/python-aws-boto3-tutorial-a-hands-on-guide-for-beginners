import boto3
import moto
import unittest


class TestCreateS3Bucket(unittest.TestCase):
    def setUp(self):
        self.s3 = boto3.client("s3")

    @moto.mock_s3
    def test_create_bucket(self):
        from create_s3_bucket_client import create_bucket_using_client

        # name of the bucket you want to create
        bucket_name = "my-new-bucket"
        bucket_region = "ap-south-1"

        # create the bucket
        create_bucket_using_client(bucket_name, bucket_region)

        # check if the bucket was created successfully
        response = self.s3.list_buckets()
        self.assertIn(bucket_name, [bucket['Name'] for bucket in response['Buckets']])

if __name__ == '__main__':
    unittest.main()