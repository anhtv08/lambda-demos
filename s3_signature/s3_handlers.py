import boto3
import logging
from botocore.exceptions import ClientError

""" a simple example using lambda function to 
  get event from s3 when new object created and created a pre-signed url to the object
  once its completed then send a notification to sqs queue

"""
s3_client = boto3.client('s3')
sqs_client = boto3.client('sqs')


def create_presigned_url(s3_client, bucket_name, object_name, expirations=3600):
    """Generate a presigned URL to share an S3 object

        :type bucket_name: string
        :param bucket_name
        :type object_name : string
        :param object_name
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
     """

    try:
        response = s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_name
            },
            ExpiresIn=expirations
        )

        print("pre-signed-url: " + response)

        print("Update alias of lambda function")
        return response
    except ClientError as e:
        logging.error(e)
        return None


def send_sign_url_to_queue(sqs_client, queue_url, pre_signed_url):
    """
    :param queue_url: String
    :param pre_signed_url: String
    :return:
    """
    sqs_response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=pre_signed_url
    )


def upload_file_to_s3(s3_client, source_file, bucket_name):
    try:
        s3_client.upload_file(source_file, bucket_name)

    except ClientError as e:
        logging.error(e)
        return None


def generate_signed_urls(records):
    signed_url = []
    for record in records:
        bucket_name = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        val_presigned_url = create_presigned_url(
            s3_client=s3_client,
            bucket_name=bucket_name,
            object_name=key
        )
        signed_url.append(val_presigned_url)


def lambda_handler(event, context):
    print(context)

    # queue_url_endpoint = context['client_context']['evn']['queue_ur']
    # print("passing queue_url from context:" + queue_url_endpoint)
    records = event['Records']
    return generate_signed_urls(records)
