#!/usr/bin/env python3

"""
This scripts lists S3 buckets using Boto3 resource
"""

import boto3

def list_s3_buckets():
    s3 = boto3.resource('s3')
    buckets = s3.buckets.all()
    return [bucket.name for bucket in buckets]


if __name__ == '__main__':
    buckets = list_s3_buckets()
    for bucket_name in buckets:
        print(f"-- {bucket_name}")
