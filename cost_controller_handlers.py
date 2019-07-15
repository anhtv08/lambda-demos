from typing import Sequence
import logging as log
import boto3
from typing import Dict
from typing import List


ec2_client = boto3.client('ec2')

ec2_resource = boto3.client('ec2')



def evaluate_ec2_instance(ec2_client, event):
    instance_id = event['detail']['instance-id']
    instance_state = event['detail']['state']

    '''
        only perform this evaluation rule when starting an new instance
        check if instance state is pending then try to perfrom evaluation 
    '''
    if instance_state != 'pending':
        log.info('current state : ' + instance_state)
        return

    ec2_instance = ec2_resource.Instance(instance_id)

    tag_list: List[str] = []

    if ec2_instance.tags:
        for tag in ec2_instance.tags:
            tag_list.append(tag['Key'])

    if not tag_list:
        log.info("Instance having no tags at all")
        shutdown_ec2_instance(ec2_client, instance_id)
    else:
        if not validate_tag_name(tag_list):
            log.info("Required tags are not defined!")
            shutdown_ec2_instance(ec2_client, instance_id)

def shutdown_ec2_instance(ec2_client, instanceId):
    log.info("shutting down instance-id :" + instanceId)
    ec2_client.terminate_instances(
        InstanceIds=[
            instanceId
        ]
    )


def validate_tag_name(tags: List[str]):
    required_tag_names: Sequence[str] = ['environment', 'owner', 'projectName', 'costCentre']
    is_valid = True

    for required_tag in required_tag_names:
        if required_tag not in tags:
            is_valid = False
            break

    return is_valid


def lambda_handler(event, context):
    log.info(" evaluating tags of ec2 instance")
    if not event:
        log.info("event is not valid")
    else:
        evaluate_ec2_instance(ec2_client, event)
