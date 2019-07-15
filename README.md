Welcome to the AWS CodeStar sample web service
==============================================


What's Here
-----------

This is a collection of lambda functions is well organized in various categories:
- iam
- cognito
- s3 client side encryption
- config store
- cost controller
- scripts folder containing the helper function for quick deploying SAM application 

Test application
------------------

1. Run ``python -m unittest``

How deploy application?
------------------
1. Run ``sh scripts/create_bucket.sh`` for provisioning the bucket- the container for application deployment file
2. Run ``sh scripts/deploySamApp.sh`` for deploying the lambda function to aws


Post deployment Verification
------------------
1. Run ``sh scripts/test_helper.sh`` - y for an instance with required tags, and no for new instance with no tags, it should get killed by the lambda function  

Example output:

```
(venv) anhs-MBP:lambda-demos anhtrang$ sh scripts/test_helpers.sh
Create an instance with appropriate tags: (y/n):n
start 100 new instances with no tags
launching instance at index:1
Running new instance with no tag
running new ec2 micro instance
```

