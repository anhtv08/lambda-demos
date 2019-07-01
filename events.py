from json import dumps


class testEvent:
    """ The factoring class to generate simple testing event for triggering lambda function

    """

    def s3_event(self):
        s3_json_event = {
            "Records": [
                {
                    "s3": {
                        "bucket": {
                            "name": "j-test-lambda-s3",
                        },
                        "object": {
                            "key": "rule_util.py"
                        }
                    }

                },
                {
                    "s3": {
                        "bucket": {
                            "name": "j-test1-lambda-s3",
                        },
                        "object": {
                            "key": "rule_util.py"
                        }
                    }

                },
                {
                    "s3": {
                        "bucket": {
                            "name": "j-test2-lambda-s3",
                        },
                        "object": {
                            "key": "rule_util.py"
                        }
                    }

                }

            ]
        }
        json_st = dumps(s3_json_event)

        return json_st

    def dynamo_event(self):
        dynamo_event = {

        }
        return dynamo_event

    def sqs_event(self):
        return {}

    def cognito_user_pool_event(self):
        cognito_user_event = {
            "version": 1,
            "triggerSource": "string",
            "region": 'us-west-2',
            "userPoolId": "user",
            "userName": "user",
            "callerContext":
                {
                    "awsSdkVersion": "string",
                    "clientId": "1235"
                },
            "request":
                {
                    "userAttributes": {
                        "string": "string"
                    }
                },
            "response": {}
        }

        return cognito_user_event
