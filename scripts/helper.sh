#!/usr/bin/env bash

# issue temporary token
aws sts assume-role \
--role-arn arn:aws:iam::674028589551:role/my-s3-readonly-role \
--role-session-name access-s3-temp-token \
--duration-seconds  3600 \
--profile my-s3-readonly-profile

