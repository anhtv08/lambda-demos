from s3_signature import s3_handlers
import unittest
import botocore
from botocore.stub import Stubber

s3_client = botocore.session.get_session().create_client('s3')
sqs_client = botocore.session.get_session().create_client('sqs')


class TestHandlerS3SigningRequest(unittest.TestCase):

    def setUp(self):
        self.sampleInvokingEvent = {
            "Records": [
                {
                    "eventVersion": "2.1",
                    "eventSource": "aws:s3",
                    "awsRegion": "us-west-2",
                    "eventTime": "1970-01-01T00:00:00.000Z",
                    "eventName": "event-type",
                    "userIdentity": {
                        "principalId": "Amazon-customer-ID-of-the-user-who-caused-the-event"
                    },
                    "requestParameters": {
                        "sourceIPAddress": "ip-address-where-request-came-from"
                    },
                    "responseElements": {
                        "x-amz-request-id": "Amazon S3 generated request ID",
                        "x-amz-id-2": "Amazon S3 host that processed the request"
                    },
                    "s3": {
                        "s3SchemaVersion": "1.0",
                        "configurationId": "ID found in the bucket notification configuration",
                        "bucket": {
                            "name": "j-test-lambda-s3",
                            "ownerIdentity": {
                                "principalId": "Amazon-customer-ID-of-the-bucket-owner"
                            },
                            "arn": "bucket-ARN"
                        },
                        "object": {
                            "key": "rule_util.py",
                            "size": 1024,
                            "eTag": "object eTag",
                            "versionId": "object version if bucket is versioning-enabled, otherwise null",
                            "sequencer": "a string representation of a hexadecimal value used to determine event sequence",
                        }
                    },
                    "glacierEventData": {
                        "restoreEventData": {
                            "lifecycleRestorationExpiryTime": "The time, in ISO-8601 format, for example, 1970-01-01T00:00:00.000Z, of Restore Expiry",
                            "lifecycleRestoreStorageClass": "Source storage class for restore"
                        }
                    }
                }
            ]
        }

    def test_sign_s3_with_event_context(self):
        # bucket_name = 'test-bucket'
        # object_name = 'test.txt'
        # expected_response = 'this_is_mocked_pre_signed_ulr'
        # expected_params = {'bucket_name': 'test-bucket', 'object_name': 'test.txt'}
        # expected_pre_signed_url = 'this_is_mocked_pre_signed_ulr'

        s3_handlers.lambda_handler(
            self.sampleInvokingEvent,
            {}
        )

        # with Stubber(s3_client) as stubber:
        #     stubber.add_response('generate_presigned_url', expected_response, expected_params)
        #     stubber.activate()
        #     result = s3_handlers.create_presigned_url(
        #         s3_client,
        #         bucket_name=bucket_name,
        #         object_name=object_name
        #
        #     )
        #     s3_handlers.lambda_handler(
        #         self.sampleInvokingEvent,
        #         {}
        #
        #     )
        #
        #     assert expected_pre_signed_url == result
        #     stubber.deactivate()


if __name__ == '__main__':
    unittest.main()
