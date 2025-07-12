import boto3
import moto
import unittest


@moto.mock_s3
class TestDeleteS3Bucket(unittest.TestCase):

    def test_delete_s3_bucket_versioning_enabled(self):
        from delete_bucket import delete_s3_bucket

        # Create a test bucket
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket='test-bucket')
        s3.put_bucket_versioning(
            Bucket='test-bucket',
            VersioningConfiguration={
                'MFADelete': 'Disabled',
                'Status': 'Enabled',
            },
        )

        # Add an object to the test bucket
        s3.put_object(Bucket='test-bucket', Key='test-object', Body=b'test-data')
        s3.delete_object(Bucket='test-bucket', Key='test-object')
        s3.put_object(Bucket='test-bucket', Key='test-object1', Body=b'test-data')
        s3.put_object(Bucket='test-bucket', Key='test-object1', Body=b'test-data1')

        # Verify that the test bucket exists
        self.assertTrue(s3.list_buckets().get('Buckets', []), [{'Name': 'test-bucket'}])

        # Delete the test bucket
        delete_s3_bucket('test-bucket')

        # Verify that the test bucket no longer exists
        self.assertFalse(s3.list_buckets().get('Buckets', []), [{'Name': 'test-bucket'}])

    def test_delete_s3_bucket_versioning_disabled(self):
        from delete_bucket import delete_s3_bucket

        # Create a test bucket
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket='test-bucket')

        # Add an object to the test bucket
        s3.put_object(Bucket='test-bucket', Key='test-object', Body=b'test-data')
        s3.delete_object(Bucket='test-bucket', Key='test-object')
        s3.put_object(Bucket='test-bucket', Key='test-object1', Body=b'test-data')
        s3.put_object(Bucket='test-bucket', Key='test-object1', Body=b'test-data1')

        # Verify that the test bucket exists
        self.assertTrue(s3.list_buckets().get('Buckets', []), [{'Name': 'test-bucket'}])

        # Delete the test bucket
        delete_s3_bucket('test-bucket')

        # Verify that the test bucket no longer exists
        self.assertFalse(s3.list_buckets().get('Buckets', []), [{'Name': 'test-bucket'}])

if __name__ == '__main__':
    unittest.main()
