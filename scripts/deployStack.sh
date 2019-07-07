#!/usr/bin/env bash

aws_working_dir=$HOME/working/cloud-computing/lambda-demos
stack_name=lambda-with-env-store-test

aws cloudformation deploy \
--stack-name $stack_name \
--template-file $aws_working_dir/template.yml \
--parameter-overrides ProjectId=lambda-demos CodeDeployRole=AWSCodePipelineServiceRole-us-west-2-Aws-code-star-example

