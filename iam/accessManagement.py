import boto3
sts_client = boto3.client('sts')
def get_temp_access_token(client, role: str):
    if role is None:
        print("Role cannot be null")
    else:
        temp_sec_token = client.assume_role(
            RoleArn=role,
            RoleSessionName='testSessionToken',
            DurationSeconds=3600
        )
        print(temp_sec_token)
        return temp_sec_token['Credentials']






