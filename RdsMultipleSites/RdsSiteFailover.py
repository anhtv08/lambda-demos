import boto3
import logging as logger
from botocore.exceptions import ClientError

sqs_client = boto3.client('sqs')
rds_client = boto3.client('rds')


def promote_rds_read_replicas(
        rds_client,
        read_replica_identifer
):

    try:
        # promote the read replica as the standalone
        response = rds_client.promote_read_replica(
            DBInstanceIdentifier=read_replica_identifer,
            BackupRetentionPeriod=1,
            PreferredBackupWindow='23:00-24:00'
        )
        print(response)

    except ClientError as ex:
        logger.error(ex)


def get_read_replica_identifier(sqn_event):
    payload = sqn_event['body']
    source_identifier: str = payload['detail']['SourceIdentifier']
    des_source_identifier = source_identifier.split('.')[1] + '-read'
    return des_source_identifier


def lambda_handler(event, context):
    rds_read_replica_identifier = get_read_replica_identifier(event)
    promote_rds_read_replicas(
        rds_client=rds_client,
        read_replica_identifer=rds_read_replica_identifier
    )
