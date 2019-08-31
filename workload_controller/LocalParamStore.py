import boto3
import logging as log
from botocore.exceptions import ClientError

class LocalParamStore:

    def __init__(self, client, prefix):
        self.client = client
        self.prefix = prefix
        self.kvPair = {}
        self._load_config_()


    def _load_config_(self):
        if not self.prefix:
           try:
                response = self.client.get_parameters_by_path(
                    Path = self.prefix
                )
                if response:
                    params = response['Parameters']

                    '''
                        print out the params
                    '''
                    print(params)
                    for item in params:
                        self.kvPair[item.Name] = item.Value

           except ClientError as ex:
               log.error(ex)


    def get_item(self, key):
        if not self.kvPair :
            return self.kvPair[key]

        else:
            self._load_config_()
            return self.kvPair[key]



