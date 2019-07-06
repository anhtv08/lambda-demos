import unittest
import index
from iam.accessManagement import get_temp_access_token
import boto3
from moto import mock_sts


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


if __name__ == '__main__':
    unittest.main()
