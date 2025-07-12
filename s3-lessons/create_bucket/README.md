# Python Boto3 Course - Create S3 Bucket example

This repository contains source code examples for the [Python Boto3 Course](https://hands-on.cloud/courses/python-boto3-course/) available at [https://hands-on.cloud](https://hands-on.cloud).

Lesson: [Create S3 Bucket](https://hands-on.cloud/course/boto3-s3-create-bucket/)

## Code examples

* [create_s3_bucket_client.py](./create_s3_bucket_client.py) - Create S3 Bucket using Boto 3 client
* [create_s3_bucket_resource.py](./create_s3_bucket_resource.py) - Create S3 Bucket using Boto 3 resource

## Unit tests

* [test_create_s3_bucket_client.py](./test_create_bucket_client.py) - Test S3 Bucket creation (client) using moto
* [test_create_s3_bucket_resource.py](./test_create_bucket_resource.py) - Test S3 Bucket creation (resource) using moto

Unit test execution:

```sh
python test_create_s3_bucket_client.py

# or

python test_create_s3_bucket_resource.py
```

More Boto3 tutorials: [https://hands-on.cloud/python-boto3-tutorials/](https://hands-on.cloud/python-boto3-tutorials/)
