#!/usr/bin/env python

"""
This script tests filtering S3 buckets method (Boto3 resource) using moto library
"""

import unittest
import moto
import boto3


class TestFilterS3Buckets(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')

    @moto.mock_s3
    def test_filter_s3_buckets_using_resource(self):
        from filter_buckets_resource import filter_buckets_using_resource

        # empty bucket list
        buckets = filter_buckets_using_resource('random_key', 'random_value')
        self.assertEqual(buckets, [])

        # create a couple of buckets
        bucket = self.s3_resource.Bucket('bucket1')
        bucket.create()
        bucket.Tagging().put(
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Project',
                        'Value': 'hands-on-cloud'
                    },
                ]
            },
        )
        bucket = self.s3_resource.Bucket('bucket2')
        bucket.create()
        bucket.Tagging().put(
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
        buckets = filter_buckets_using_resource('Project', 'hands-on-cloud')
        self.assertEqual(buckets, ['bucket1'])
        buckets = filter_buckets_using_resource('Project', 'hands-on-cloud1')
        self.assertEqual(buckets, ['bucket2'])


if __name__ == '__main__':
    unittest.main()
