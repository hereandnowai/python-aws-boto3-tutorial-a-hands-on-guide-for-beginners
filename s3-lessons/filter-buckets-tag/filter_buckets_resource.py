#!/usr/bin/env python

"""
This script searches S3 buckets by Tag using Boto3 resource
"""

import boto3
import botocore


def filter_buckets_using_resource(tag_key, tag_value):
    s3_resource = boto3.resource('s3')
    bucket_iterator = s3_resource.buckets.all()

    filtered_buckets = []

    for bucket in bucket_iterator:
        try:
            bucket_tags = bucket.Tagging().tag_set
            for tag in bucket_tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    filtered_buckets.append(bucket.name)
                    break
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'NoSuchTagSet':
                pass

    return filtered_buckets


if __name__ == '__main__':
    buckets = filter_buckets_using_resource('Project', 'hands-on-cloud')
    for bucket in buckets:
        print(f'-- {bucket}')
