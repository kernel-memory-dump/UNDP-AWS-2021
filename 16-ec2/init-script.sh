#!/bin/bash
apt-get update
apt-get install nginx -y
git clone https://github.com/sebastian/UNDP
cp UNDP/* /var/www/html/
service nginx start