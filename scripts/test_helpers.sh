#!/usr/bin/env bash

# 1. launch new instance from cli

ret_instance_id=
function launch_new_instance() {
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


launch_new_instance
echo "waiting for 5 mins"
sleep 5m

#terminate_instance $ret_instance_id


#aws ec2
# 2. check instance status

#instance_id=
#aws ec2 describe-instance

# 3. wait for 5 mins, instance should changed to stopped status

