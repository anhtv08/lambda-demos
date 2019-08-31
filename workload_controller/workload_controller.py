import boto3
import logging as log
from botocore.exceptions import ClientError
import json
from workload_controller.LocalParamStore import LocalParamStore

ssm_client = boto3.client('ssm')
rds_client = boto3.client('rds')
sqs_client = boto3.client('sqs')
path_prefix='/apps/workloadsManager/dev/'
configStore={}
queue_url_key='queueUrl'

class Note:
    def __init__(self, title:str, body:str):
        self.title = title
        self.body= body


def load_config():

    configStore = LocalParamStore(
        client=ssm_client,
        prefix=path_prefix
    )


def store_message(rds_client, param):
    rds_client.store_into_db(param)


def drail_message_from_queue(sqs_client):

    try:
        response = sqs_client.receive_message(
            QueueUrl=configStore[queue_url_key],
            MaxNumberOfMessages=1,
            VisibilityTimeout=1,
            WaitTimeSeconds=123
        )

        messages = response['Messages']

        for message  in messages:
            store_message(covert_to_notes(message))

    except ClientError as ex:
        log.error(ex)


def covert_to_notes(sqs_message):
    return json.dump(sqs_message['Body'])


def lambda_handler(event, context):
    load_config()
    drail_message_from_queue(sqs_client= sqs_client)
