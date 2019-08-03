#!/usr/bin/env bash

# mounting to efs file system
sudo yum install -y amazon-efs-utils
sudo mkdir efs
sudo mount -t efs fs-4eb3ef37:/ efs
