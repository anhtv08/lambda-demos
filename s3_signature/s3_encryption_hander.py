import boto3
from s3_encryption.client import S3EncryptionClient

s3_client = boto3.client('s3')
def encrypt_and_upload_file(s3EncryptionClient: S3EncryptionClient , config):

    file_name = config['file_name']
    bucket_name = config['bucket_name']
    encryption_key = config['encryption_key']

    s3EncryptionClient.put_object(
        file_name,
        bucket_name,
        encryption_key
    )


def print_transferred_data(bytes):
    print("Bytes transferred :" + bytes)
def upload_file(client, file_name, bucket_name, object_key):

    with open(file_name, 'rb') as data:
        client.upload_fileobj(data, bucket_name, object_key, print_transferred_data)


if __name__ == '__main__':

    s3e = S3EncryptionClient()
    encrypt_and_upload_file(
        s3e,
        config={
            "bucket_name": "joey-s3-bucket",
            "file_name": "test.txt",
            "encryption_key": "sjfoijsfo"
        }
    )

