from typing import Sequence
import logging as log
import boto3
ec2_client = boto3.client('ec2')

def release_ip_address():
    return None

def lambda_handler(event, context):
    log.info("releasing elastic IP address when its not running")
    if not event:
        log.info("event is not valid")
    else:
        release_ip_address(ec2_client, event)