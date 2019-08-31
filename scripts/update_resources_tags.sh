#!/usr/bin/env bash

# using ssm to update tags for all ec2 isntances

# tags required: env=[dev,uat,prod], costCentre=[], projectName=<your proeject name>

aws ssm add-tags-to-resource \
--resource-type "MaintenanceWindow" \
--resource-id "i-0a2c4ffa17d8bfe32" \
--tags "Key=env,Value=dev,Key=CostCentre,Value=123,Key=ProjectName,Value=Aws"



