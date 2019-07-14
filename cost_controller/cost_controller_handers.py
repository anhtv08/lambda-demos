from typing import Dict
from typing import Sequence
import boto3

sts_client = boto3.client('sts')

ec2_client = boto3.client('ec2')

sqs_client = boto3.client('sqs')


def evaluate_ec2_instance(ec2_client, event):
    instance_id = event['detail']['instance-id']
    instance_state = event['detail']['state']

    '''
        only perform this evaluation rule when starting an new instance
        check if instance state is pending then try to perfrom evaluation 
    '''
    if instance_state != 'pending':
        return

    InstanceIds = [
                      instance_id
                  ],

    ec2_instance_details = ec2_client.describe_instances(
        InstanceIds=InstanceIds
    )

    if not ec2_instance_details:

        tags: [Dict[str, str]] = ec2_instance_details['Reservations'][0]['Instances']['Tags']

        '''
         if not tags then terminate the instance
         mandatory tags names are not provided then shutdown also
        '''
        if not tags:
            shutdown_ec2_instance(ec2_client, instance_id)
        else:
            if not validate_tag_name(tags):
                shutdown_ec2_instance(ec2_client, instance_id)


def shutdown_ec2_instance(ec2_client, instanceId):
    ec2_client.stop_instances(
        InstanceIds=[
            instanceId
        ]
    )


def validate_tag_name(tag: Dict[str, str]):
    allowed_tag_names: Sequence[str] = ['environment', 'owner', 'projectName', 'costCentre']
    for item in tag:
        if item not in allowed_tag_names:
            return False


def lambda_handler(event, context):
    print(" evaluating tags of ec2 instance")
    if not event:
        evaluate_ec2_instance(ec2_client, event)
    else:
        print("event is not valid")
