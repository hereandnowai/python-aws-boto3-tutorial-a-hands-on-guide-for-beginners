#!/usr/bin/env python

"""
This script search S3 buckets by Tag using Boto3 client
"""

import boto3
import botocore

def filter_buckets_using_client(tag_key, tag_value):
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()

    filtered_buckets = []

    buckets = response['Buckets']

    for bucket in buckets:
        try:
            bucket_name = bucket['Name']
            bucket_tags = s3_client.get_bucket_tagging(Bucket=bucket_name)['TagSet']
            for tag in bucket_tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    filtered_buckets.append(bucket_name)
                    break
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'NoSuchTagSet':
                pass

    return filtered_buckets


if __name__ == '__main__':
    buckets = filter_buckets_using_client('Project', 'hands-on-cloud')
    for bucket in buckets:
        print(f'-- {bucket}')
