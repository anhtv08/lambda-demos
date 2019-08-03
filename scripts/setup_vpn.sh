#!/usr/bin/env bash

# reference links:
#https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-18-04


#Step 1: Install OpenVPN
sudo apt-get update
sudo apt-get install openvpn easy-rsa

#Step 2: Set Up the CA Directory
make-cadir ~/openvpn-ca

#Step 3: Configure the CA Variables
./clean-all
./build-ca

#Step 5: Create the Server Certificate, Key, and Encryption Files

./build-key-server server

./build-dh

openvpn --genkey --secret keys/ta.key

#Step 6: Generate a Client Certificate and Key Pair




#!/bin/bash

# First argument: Client identifier

KEY_DIR=~/client-configs/keys
OUTPUT_DIR=~/client-configs/files
BASE_CONFIG=~/client-configs/base.conf

cat ${BASE_CONFIG} \
    <(echo -e '<ca>') \
    ${KEY_DIR}/ca.crt \
    <(echo -e '</ca>\n<cert>') \
    ${KEY_DIR}/${1}.crt \
    <(echo -e '</cert>\n<key>') \
    ${KEY_DIR}/${1}.key \
    <(echo -e '</key>\n<tls-auth>') \
    ${KEY_DIR}/ta.key \
    <(echo -e '</tls-auth>') \
    > ${OUTPUT_DIR}/${1}.ovpn