#!/bin/bash
apt-get update
apt-get install nginx -y
apt-get install git -y
rm -rf /var/www/html/index.html
mkdir app
cd app
git clone https://github.com/kernel-memory-dump/UNDP-boto3-test.git
cd UNDP-boto3-test
cp -r . /var/www/html/
service nginx start
# startuj nginx nakon reboot-a ako se rebootuje masina
chkconfig nginx on