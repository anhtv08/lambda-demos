#!/usr/bin/env bash

aws_working_dir=$HOME/working/cloud-computing/lambda-demos

for i in {1..100}; do

echo "putting metric at index :$i"
aws cloudwatch put-metric-data \
--namespace  my-custom-metric-test \
--metric-data file://metric_data_file.json &

wait

done






