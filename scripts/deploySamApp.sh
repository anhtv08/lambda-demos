#!/usr/bin/env bash

revision=$1

bucket_name=joey-my-sam-app
aws s3 mb s3://bucketname


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# packaging application
sam package \
    --output-template-file $DIR/packaged.yaml \
    --s3-bucket $bucket_name


# deploying application
sam deploy \
    --template-file $$DIR/packaged.yaml \
    --stack-name sam-app \
    --capabilities CAPABILITY_IAM \
