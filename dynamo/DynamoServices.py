import boto3
import logging as logger
from botocore.exceptions import ClientError
dynamo_client = boto3.client('dynamodb')

class Person:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name;
        self.last_name = last_name
        self.email = email
        self.age = age


def handle_exception(ex):
    if ex.response['Error']['Code'] == 'EntityAlreadyExists':
        print("User already exists")
    else:
        print("Unexpected error: %s" % ex)


def add_user(client, person: Person):
    """
    Adding store a dummy user into dynamo
    :param client:
    :param person:
    :return:
    """
    try:
        client.put_item(
            TableName='user_tbl',
            Item={
                'first_name': {'S': person.first_name},
                'last_name': {'S': person.last_name},
                'age': {'S': person.age},
                'email': {'S': person.email},
            }
        )
    except ClientError as ex:
        handle_exception(ex)


def create_dummy_user():
    return Person(
        first_name='anh',
        last_name='trang',
        email='joeytrang88@gmail.com',
        age='10'
    )


def lambda_handler(event, context):
    person = create_dummy_user()
    add_user(dynamo_client, person)
    if not event:
        logger.info("event is not valid")
    else:
        print("""
             Todo:
        """)
        # evaluate_ec2_instance(ec2_client, event)
