import unittest
import index
from cost_controller import cost_controller_handlers
import boto3
from events import testEvent
from moto import mock_ec2


class TestHandlerCase(unittest.TestCase):

    # @mock_sts
    # def test_get_sts_token(self):
    #     sts_client = boto3.client('sts')
    #     identity = sts_client.get_caller_indentity()
    #     print(identity)

    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World', result['body'])

    def test_evaluate_instance_tags(self):
        # Given full required tags
        tags = ['environment', 'owner', 'projectName', 'costCentre']

        result = cost_controller_handlers.validate_tag_name(tags)
        self.assertTrue(result)

        # given missing required tags:

        tags.clear()

        tags = ['environment', 'owner', 'projectName']

        result = cost_controller_handlers.validate_tag_name(tags)
        self.assertFalse(result)

        # no tags provided:

        tags.clear()
        result = cost_controller_handlers.validate_tag_name(tags)
        self.assertFalse(result)

    @mock_ec2
    def test_evaluate_ec2_instance(self):
        testStateChangeEven = testEvent()
        ec2_client = boto3.client('ec2', region_name='us-east-2')

        cost_controller_handlers.evaluate_ec2_instance(
            ec2_client,
            testStateChangeEven.ec2_state_changes()
        )
        ec2_instances = ec2_client.describe_instances()['Reservations'][0]['Instances']
        assert len(ec2_instances) == 1


if __name__ == '__main__':
    unittest.main()
