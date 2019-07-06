#!/usr/bin/env bash

aws_working_dir=$HOME/working/cloud-computing/lambda-demos


echo "putting following metric data to cloud watch: $metric_data_test"
aws cloudwatch put-metric-data \
--namespace  my-custom-metric-test \
--metric-data file://metric_data_file.json






