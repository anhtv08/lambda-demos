import unittest
import index
import cost_controller_handlers
from typing import Dict


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


if __name__ == '__main__':
    unittest.main()
