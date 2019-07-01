import boto3
import logging
from botocore.exceptions import ClientError

kinesis_client = boto3.client('kinesis')


def send_stream_event_kinesis(kinesis_client, stream_name, user_id, client_id):
    data = "userName : {}, client_id: {}".format(user_id, client_id)

    if not user_id and not client_id:

        try:

            response = kinesis_client.put_record(
                StreamName=stream_name,
                Data=data,
                PartitionKey=user_id,
                ExplicitHashKey=user_id

            )
            print(response)
        except ClientError as e:
            logging.error(e)
            return None


def lambda_handler(event, context):
    user_id = event['userName']
    client_id = event['callerContext']['clientId']
    stream_name = context['stream_name']

    send_stream_event_kinesis(
        kinesis_client=kinesis_client,
        stream_name=stream_name,
        user_id=user_id,
        client_id=client_id
    )
