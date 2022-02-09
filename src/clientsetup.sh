#!/bin/bash
chmod 700 micsetup.sh
sh micsetup.sh

USER=$1
IP=$2

ssh-keygen -o
cd ~/.ssh/
scp -o PubkeyAuthentication=no id_rsa.pub $USER@$IP:~/.ssh/authorized_keys2