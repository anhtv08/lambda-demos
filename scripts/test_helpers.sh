#!/usr/bin/env bash

# 1. launch new instance from cli

ret_instance_id=

function run_new_instance_with_tags() {
    iam_id=ami-0d8f6eb4f641ef691
    instance_type=t2.micro
    key_pair_name=my_ec2_kp
    sub_net_id=subnet-0876ad10627174bc8
    vpc_id=vpc-d43addbf

    echo "running new ec2 micro instance with appropriate tags"
    ret_instance_id=$(aws ec2 run-instances \
    --image-id $iam_id --count 1 \
    --instance-type $instance_type \
    --key-name $key_pair_name \
    --tag-specifications "ResourceType=instance,Tags=[{Key=environment,Value=111},{Key=owner,Value=11}, {Key=projectName,Value=11}, {Key=costCentre,Value=11}]" \
    --subnet-id $sub_net_id | jq ".Instances[0].InstanceId" | sed -e 's/^"//' -e 's/"$//')
    echo "launched instance: $ret_instance_id"
    aws ec2 describe-instances --instance-ids $ret_instance_id


}
function launch_new_instance() {
    echo "Running new instance with no tag"
    iam_id=ami-0d8f6eb4f641ef691
    instance_type=t2.micro
    key_pair_name=my_ec2_kp
    sub_net_id=subnet-0876ad10627174bc8
    vpc_id=vpc-d43addbf

    echo "running new ec2 micro instance"
    ret_instance_id=$(aws ec2 run-instances \
    --image-id $iam_id --count 1 \
    --instance-type $instance_type \
    --key-name $key_pair_name \
    --subnet-id $sub_net_id | jq ".Instances[0].InstanceId" | sed -e 's/^"//' -e 's/"$//')

    echo "launched instance: $ret_instance_id"
    aws ec2 describe-instances --instance-ids $ret_instance_id

}

function terminate_instance() {
    echo "terminating instance after 5 mins"
    local instance_id_to_kill=$1
    aws ec2 terminate-instances --instance-ids $instance_id_to_kill

}

with_tag='n'
read -p 'Create an instance with appropriate tags: (y/n):' with_tag

if [[ $with_tag == 'y' ]]; then
    run_new_instance_with_tags
else
   echo "start 100 new instances with no tags"

   for i in `seq 1`; do
    echo "launching instance at index:$i"
    launch_new_instance
   done

fi
#

echo "waiting for 5 mins"
sleep 5m

#terminate_instance $ret_instance_id


#aws ec2
# 2. check instance status

#instance_id=
#aws ec2 describe-instance

# 3. wait for 5 mins, instance should changed to stopped status