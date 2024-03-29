#!/usr/bin/env bash

function create_new_dynamo_tbl() {
    aws dynamodb  \
     create-table \
    --attribute-definitions AttributeName='email',AttributeType='S' \
    --table-name 'user_tbl' \
    --key-schema AttributeName='email',KeyType='HASH' \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

}

function create_new_bucket() {
    aws s3 mb s3://joey-my-sam-app
}

function create_test_rds() {

    local db_name='MyTestDb'
    local user_name='admin'
    local password='admin123'
    local db_sg_group='mygs-myrds-public'
    local db_subnet_group='my-rds-subnet-group'

    aws rds create-db-instance \
    --db-name $db_name \
    --db-instance-identifier $db_name \
    --allocated-storage 5 \
    --db-instance-class 'db.t2.micro' \
    --engine 'MySQL' \
    --master-username $user_name \
    --db-subnet-group-name $db_subnet_group \
    --master-user-password $password

}

function create_public_ec2() {
    aws ec2
}

function main() {
    local obj_type=$1
    case $obj_type in
        dynamo)
            create_new_dynamo_tbl
            ;;
        s3)
            create_new_bucket
            ;;
        rds)
           create_test_rds
           ;;
        *)
             echo "invalid option"
    esac

}
obj_type=$1
main $obj_type