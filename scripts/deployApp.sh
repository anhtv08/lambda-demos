#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

REVISION=$1

if [[ -z "$REVISION" ]]; then
	echo "No revision specified!"
	exit 1
fi

STACK_OUTPUTS=`aws cloudformation describe-stacks --stack-name webapp-example --query "Stacks[0].Outputs[].[OutputValue]" --output text`
DEPLOYMENT_BUCKET=`echo "$STACK_OUTPUTS" | grep webappdeploymentbucket`
DEPLOYMENT_GROUP=`echo "$STACK_OUTPUTS" | grep WebappDeploymentGroup`
APPLICATION_NAME=`echo "$STACK_OUTPUTS" | grep WebappApplication`

aws deploy push --application-name $APPLICATION_NAME \
	--s3-location s3://$DEPLOYMENT_BUCKET/$REVISION \
	--source $DIR/../webapp > /dev/null

aws deploy create-deployment --application-name $APPLICATION_NAME \
	--s3-location bucket="$DEPLOYMENT_BUCKET",key="$REVISION",bundleType=zip \
	--deployment-group-name $DEPLOYMENT_GROUP


declare -a arr=(aws-codestar-us-west-2-504441261471 aws-codestar-us-west-2-504441261471-aws-code-star-e-pipe aws-codestar-us-west-2-504441261471-aws-code-star-w-pipe code-star-config-bucket elasticbeanstalk-us-east-1-504441261471 elasticbeanstalk-us-east-2-504441261471 elasticbeanstalk-us-west-2-504441261471 j-bucket-with-encryption j-my-flowlogs j-my-shared-bucket joey-aws-test-provision joey-mytestbucket joey-textract-console-us-west-2 textract-console-us-west-2-5bcf13e1-91ea-4396-9597-066673992ebc)

for item in "${arr[@]}"; do
    aws s3 rb s3://$item --force --recursive --profile joey-cli-devops-admin
done
