#!/bin/env python

"""
This test validates list of S3 buckets returned by list_s3_buckets method
"""

import boto3
import moto
import unittest


class TestListS3Buckets(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')

    @moto.mock_s3
    def test_list_s3_buckets(self):
        from list_buckets_client import list_s3_buckets

        bucket_names = list_s3_buckets()
        self.assertEqual(bucket_names, [])

        self.s3_resource.create_bucket(Bucket='bucket1')
        self.s3_resource.create_bucket(Bucket='bucket2')
        self.s3_resource.create_bucket(Bucket='bucket3')

        bucket_names = list_s3_buckets()
        self.assertEqual(bucket_names, ['bucket1', 'bucket2', 'bucket3'])


if __name__ == '__main__':
    unittest.main()
