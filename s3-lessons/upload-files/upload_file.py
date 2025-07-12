import io
import logging
import boto3
import botocore

logger = logging.getLogger()
logging.getLogger("boto3").setLevel(logging.WARNING)
logging.getLogger("botocore").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

S3_CLIENT = boto3.client('s3')

def upload_file_to_s3(file_name, bucket, object_name=None, args=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :param args: Additional arguments to S3 client
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    try:
        response = S3_CLIENT.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    except botocore.exceptions.ClientError as error:
        logging.error(error)
        return False
    return True

def upload_generated_file_object_to_s3(bucket, object_name, args=None):
    """
    Upload a file object to an S3 bucket

    :param bucket: Bucket to upload to
    :param object_name: S3 object name
    :param args: Additional arguments to S3 client
    :return: True if file was uploaded, else False
    """

    with io.BytesIO() as f:
        # Create a text file object in memory
        f.write(b'First line.\n')
        f.write(b'Second line.\n')
        f.seek(0)

        try:
            S3_CLIENT.upload_fileobj(f, bucket, object_name, ExtraArgs=args)
        except botocore.exceptions.ClientError as error:
            logging.error(error)
            return False
        return True
