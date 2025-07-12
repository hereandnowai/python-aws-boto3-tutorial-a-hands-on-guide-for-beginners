# Python Boto3 Course - Filter S3 Buckets by Tag example

This repository contains source code examples for the [Python Boto3 Course](https://hands-on.cloud/courses/python-boto3-course/) available at [https://hands-on.cloud](https://hands-on.cloud).

Lesson: [Filter S3 Buckets (by Tag)](https://hands-on.cloud/course/boto3-s3-filter-buckets-tag/)

## Code examples

* [filter_buckets_client.py](./filter_buckets_client.py) - Filter S3 Buckets by Tag using Boto 3 client
* [filter_buckets_resource.py](./filter_buckets_resource.py) - Filter S3 Buckets by Tag using Boto 3 resource

## Unit tests

* [test_filter_buckets_client.py](./test_filter_buckets_client.py) - Test S3 Bucket filter method (Boto3 client) using moto
* [test_filter_buckets_resource.py](./test_filter_buckets_resource.py) -  Test S3 Bucket filter method (Boto3 resource) using moto

Unit test execution:

```sh
python test_filter_buckets_client.py

# or

python test_filter_buckets_resource.py
```

More Boto3 tutorials: [https://hands-on.cloud/python-boto3-tutorials/](https://hands-on.cloud/python-boto3-tutorials/)
