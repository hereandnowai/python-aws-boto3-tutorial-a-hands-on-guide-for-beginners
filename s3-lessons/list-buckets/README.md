# Python Boto3 Course - List S3 Buckets example

This repository contains source code examples for the [Python Boto3 Course](https://hands-on.cloud/courses/python-boto3-course/) available at [https://hands-on.cloud](https://hands-on.cloud).

Lesson: [List S3 Buckets](https://hands-on.cloud/course/boto3-s3-list-buckets/)

## Code examples

* [list_buckets_client.py](./list_buckets_client.py) - Lists S3 Buckets using Boto 3 client
* [list_buckets_resource.py](./list_buckets_resource.py) - Lists S3 Buckets using Boto 3 resource

## Unit tests

* [test_list_buckets_client.py](./test_list_buckets_client.py) - Test S3 Bucket list operation (Boto3 client) using moto
* [test_create_s3_bucket_resource.py](./test_create_bucket_resource.py) - Test S3 Bucket list operation (Boto3 resource) using moto

Unit test execution:

```sh
python test_list_buckets_client.py

# or

python test_create_s3_bucket_resource.py
```

More Boto3 tutorials: [https://hands-on.cloud/python-boto3-tutorials/](https://hands-on.cloud/python-boto3-tutorials/)
