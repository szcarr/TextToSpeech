#!/bin/bash

USER=$1
FILENAME=$2
IP=$3 
FILEPATH=$4
# -o PubkeyAuthentication=no
scp $FILENAME $USER@$IP:$FILEPATH