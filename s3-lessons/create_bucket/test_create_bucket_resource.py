import boto3
import moto
import unittest
from create_s3_bucket_resource import create_bucket_using_resource

class TestCreateS3Bucket(unittest.TestCase):
    def setUp(self):
        self.s3 = boto3.resource("s3")

    @moto.mock_s3
    def test_create_bucket(self):
        # name of the bucket you want to create
        bucket_name = "my-new-bucket"
        bucket_region = "ap-south-1"

        # create the bucket
        create_bucket_using_resource(bucket_name, bucket_region)

        # check if the bucket was created successfully
        buckets = self.s3.buckets.all()
        self.assertIn(bucket_name, [bucket.name for bucket in buckets])

if __name__ == '__main__':
    unittest.main()
