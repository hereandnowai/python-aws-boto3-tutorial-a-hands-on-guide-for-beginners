#!/usr/bin/env python

"""
This script tests filtering S3 buckets method (Boto3 client) using moto library
"""

import unittest
import moto
import boto3


class TestFilterS3Buckets(unittest.TestCase):
    def setUp(self):
        self.s3_client = boto3.client('s3')

    @moto.mock_s3
    def test_filter_s3_buckets_using_client(self):
        from filter_buckets_client import filter_buckets_using_client

        # empty bucket list
        buckets = filter_buckets_using_client('random_key', 'random_value')
        self.assertEqual(buckets, [])

        # create a couple of buckets
        self.s3_client.create_bucket(Bucket='bucket1')
        self.s3_client.put_bucket_tagging(
            Bucket='bucket1',
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Project',
                        'Value': 'hands-on-cloud'
                    },
                ]
            },
        )
        self.s3_client.create_bucket(Bucket='bucket2')
        self.s3_client.put_bucket_tagging(
            Bucket='bucket2',
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Project',
                        'Value': 'hands-on-cloud1'
                    },
                ]
            },
        )

        # test that all created buckets are returned by our method
        buckets = filter_buckets_using_client('Project', 'hands-on-cloud')
        self.assertEqual(buckets, ['bucket1'])
        buckets = filter_buckets_using_client('Project', 'hands-on-cloud1')
        self.assertEqual(buckets, ['bucket2'])


if __name__ == '__main__':
    unittest.main()
