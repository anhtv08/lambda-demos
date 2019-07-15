Welcome to the AWS CodeStar sample web service
==============================================

This is a collection of lambda functions is well organized in various categories:
- iam
- cognito
- s3 client side encryption
- config store
- cost controller
- scripts folder containing the helper function for quick deploying SAM application 

What's Here
-----------

This sample includes:

* README.md - this file
* template.yml - this file contains the AWS Serverless Application Model (AWS SAM) used
  by AWS CloudFormation to deploy your application to AWS Lambda and Amazon API
  Gateway.
* tests/ - this directory contains unit tests for your application



Test application
------------------

1. Run ``python -m unittest``

How deploy application?
------------------
1. Run ``sh scripts/create_bucket.sh`` for provisioning the bucket- the container for application deployment file
2. Run ``sh scripts/deploySamApp.sh`` for deploying the lambda function to aws


Verify deployment?
------------------
1. Run ``sh scripts/test_helper.sh 0`` for creating the ec2 instance with no tag, it should get terminated by the lambda function
2. Run ``sh scripts/test_helper.sh 1`` for creating the ec2 instance with required tags, it should get started normally
