# Python Boto3 Course - S3 Batch Operations example

This repository contains source code examples for the [Python Boto3 Course](https://hands-on.cloud/courses/python-boto3-course/) available at [https://hands-on.cloud](https://hands-on.cloud).

Lesson: [Upload file to S3 bucket](https://hands-on.cloud/course/boto3-s3-batch-operations/)

## Code examples

* [upload_files.py](./upload_files.py) - Upload multiple files into S3 bucket using Boto 3 and multithreading
* [download_files.py](./download_files.py) - Download multiple files from S3 bucket using Boto 3 and multithreading
* [sync_folder_upload.py](./sync_folder_upload.py) - Synchronize local folder into S3 bucket using Boto 3 and multithreading
* [sync_folder_download.py](./sync_folder_download.py) - Synchronize S3 bucket objects into local folder using Boto 3 and multithreading

## Unit tests

* [test_upload_files.py](./test_upload_files.py) - Upload multiple files into S3 bucket using Boto 3 and multithreading
* [test_download_files.py](./test_download_files.py) - Download multiple files from S3 bucket using Boto 3 and multithreading
* [test_sync_folder_upload.py](./test_sync_folder_upload.py) - Synchronize local folder into S3 bucket using Boto 3 and multithreading
* [test_sync_folder_download.py](./test_sync_folder_download.py) - Synchronize S3 bucket objects into local folder using Boto 3 and multithreading

Unit test execution:

```sh
python test_upload_files.py
python test_download_files.py
python test_sync_folder_upload.py
python test_sync_folder_download.py
```

More Boto3 tutorials: [https://hands-on.cloud/python-boto3-tutorials/](https://hands-on.cloud/python-boto3-tutorials/)
