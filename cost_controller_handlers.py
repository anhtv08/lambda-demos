from typing import Dict
from typing import Sequence
import logging as log
import boto3

ec2_client = boto3.client('ec2')


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

    InstanceIds = [
                      instance_id
                  ]

    ec2_instance_details = ec2_client.describe_instances(
        InstanceIds=InstanceIds
    )

    if ec2_instance_details:

        log.info(ec2_instance_details)
        try:
            tags: [Dict[str, str]] = ec2_instance_details['Reservations'][0]['Instances'][0]['Tags']
            log.info(tags)

            '''
             if not tags then terminate the instance
             mandatory tags names are not provided then shutdown also
            '''
            if not tags:
                log.info("Instance having no tags at all")
                shutdown_ec2_instance(ec2_client, instance_id)
            else:
                if not validate_tag_name(tags):
                    log.info("Required tags are not defined!")
                    shutdown_ec2_instance(ec2_client, instance_id)
        except Exception as ex:
            log.debug(ex)
            log.info("There are is not tag, shutting down the instance id : " + instance_id)
            shutdown_ec2_instance(ec2_client, instance_id)


def shutdown_ec2_instance(ec2_client, instanceId):
    log.info("shutting down instance-id :" + instanceId)
    ec2_client.terminate_instances(
        InstanceIds=[
            instanceId
        ]
    )


def validate_tag_name(tags: Dict[str, str]):
    required_tag_names: Sequence[str] = ['environment', 'owner', 'projectName', 'costCentre']
    key_tags = tags.keys()

    is_valid = True

    for required_tag in required_tag_names:
        if required_tag not in key_tags:
            is_valid = False
            break

    return is_valid


def lambda_handler(event, context):
    log.info(" evaluating tags of ec2 instance")
    if not event:
        log.info("event is not valid")
    else:
        evaluate_ec2_instance(ec2_client, event)
