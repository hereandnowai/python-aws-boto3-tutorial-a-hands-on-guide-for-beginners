#!/usr/bin/env python3
"""
This script demonstrates how to create S3 bucket using Boto3 S3 client
"""

import boto3

BUCKET_NAME='hands-on-cloud-demo-bucket-client'
AWS_REGION='us-east-2'


def create_bucket_using_client(bucket_name, region):
    location = {'LocationConstraint': region}

    s3_client = boto3.client("s3", region_name=region)

    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration=location
    )

    return response

if __name__ == '__main__':
    response = create_bucket_using_client(BUCKET_NAME, AWS_REGION)
    print(f"Amazon S3 bucket '{BUCKET_NAME}' has been created")
