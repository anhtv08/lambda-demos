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

function main() {
    local obj_type=$1
    case $obj_type in
        dynamo)
            create_new_dynamo_tbl
            ;;
        s3)
            create_new_bucket
            ;;
        *)
             echo "invalid option"
    esac

}
obj_type=$1
main $obj_type