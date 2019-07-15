#!/usr/bin/env bash

bucket_name=joey-my-sam-app
project_dir=$HOME/working/cloud-computing/lambda-demos

# packaging application
sam package \
    --output-template-file $project_dir/output/packaged.yaml \
    --s3-bucket $bucket_name > /dev/null


# deploying application

echo "Deploying lambda functions:"
sam deploy \
    --template-file $project_dir/output/packaged.yaml \
    --stack-name sam-app-1 \
    --capabilities CAPABILITY_IAM