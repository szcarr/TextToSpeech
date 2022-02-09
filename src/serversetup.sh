#!/bin/bash

USER=$1
IP=$2 

ssh-keygen -o
cd ~/.ssh/
scp -o PubkeyAuthentication=no id_rsa.pub $USER@$IP:~/.ssh/authorized_keys2