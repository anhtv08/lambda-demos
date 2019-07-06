#!/usr/bin/env bash

aws_working_dir=$HOME/working/cloud-computing/lambda-demos
start=$1
end=$2
start_index=$start

# using seq function to iterate.

echo "generating sequence from $start to $end"
for i in `seq $end`; do
    echo "putting metric at index :$i"
    aws cloudwatch put-metric-data \
    --namespace  my-custom-metric-test \
    --metric-data file://metric_data_file.json
    let start=start+1
done

