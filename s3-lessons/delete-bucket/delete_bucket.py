#!/usr/bin/env python

'''
This script cleans up and deletes Amazon S3 bucket
'''

import boto3

S3_CLIENT = boto3.client('s3')
S3_RESOURCE = boto3.resource('s3')

def delete_s3_bucket_versions(bucket_name, object_versions):
    # Get all object versions
    versions = object_versions.get('Versions', [])

    if versions:
        delete_keys = {'Objects': [{'Key': version['Key'], 'VersionId': version['VersionId']} for version in versions]}
        S3_CLIENT.delete_objects(Bucket=bucket_name, Delete=delete_keys)

def delete_s3_bucket_delete_markers(bucket_name, object_versions):
    # Get all object versions in the bucket's versioning-enabled delete marker
    delete_markers = object_versions.get('DeleteMarkers', [])

    if delete_markers:
        # Delete all object versions in the bucket's versioning-enabled delete marker
        delete_marker_keys = {'Objects': [{'Key': marker['Key'], 'VersionId': marker['VersionId']} for marker in delete_markers]}
        S3_CLIENT.delete_objects(Bucket=bucket_name, Delete=delete_marker_keys)

def delete_s3_bucket(bucket_name):
    # Get all object versions
    object_versions = S3_CLIENT.list_object_versions(Bucket=bucket_name, MaxKeys=1000)

    while True:
        # Delete all object versions
        delete_s3_bucket_versions(bucket_name, object_versions)

        # Delete all delete markers
        delete_s3_bucket_delete_markers(bucket_name, object_versions)

        # Check if there are more object versions to delete
        if object_versions.get('IsTruncated'):
            object_versions = S3_CLIENT.list_object_versions(Bucket=bucket_name, MaxKeys=1000, KeyMarker=object_versions['NextKeyMarker'], VersionIdMarker=object_versions['NextVersionIdMarker'])
        else:
            break

    # Deleting S3 bucket
    S3_RESOURCE.Bucket(bucket_name).delete()

if __name__ == '__main__':
    delete_s3_bucket('my-s3-bucket')
