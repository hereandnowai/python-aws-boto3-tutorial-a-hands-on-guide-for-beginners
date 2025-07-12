#!/usr/bin/env python3
"""
This script demonstrates how to create S3 bucket using Boto3 S3 resource
"""

import boto3

BUCKET_NAME='hands-on-cloud-demo-bucket-resource'
AWS_REGION='us-east-2'


def create_bucket_using_resource(bucket_name, region):
    location = {'LocationConstraint': region}

    s3_resource = boto3.resource("s3", region_name=region)

    bucket = s3_resource.Bucket(bucket_name)
    bucket.create(
        CreateBucketConfiguration=location
    )

    return bucket

if __name__ == '__main__':
    bucket = create_bucket(BUCKET_NAME, AWS_REGION)
    print(f"Amazon S3 bucket '{bucket.name}' has been created")
