import boto3
import base64
import time

import os

user_data = """#!/bin/bash
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
"""

user_data_base64 = base64.b64encode(bytes(user_data, 'utf-8'))


ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
REGION = os.environ['AWS_REGION']

dry_ryn = False; # useful variable to put the script into dry run mode where the function allows it

ec2_client = boto3.client('ec2', 
   aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY, region_name=REGION)
e2_resource = boto3.resource('ec2',    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY, region_name=REGION)


print("Launching a new EC2 INSTANCE")
# Create the instance 
instances = e2_resource.create_instances(
    DryRun = False,
    ImageId = "ami-05f7491af5eef733a",
    InstanceType = "t2.micro",
    SecurityGroupIds = ["sg-02f0d08a40e10b9bd"],
    MinCount = 1,
    MaxCount = 1,
    UserData = user_data
)

instance = instances[0]
print(f"EC2 instance launched {instance.instance_id}")
print("WAITING UNTIL started")

instance.wait_until_running()
print("THE NEW Ec2 instance is READY")
# pokusacemo 100x da dobijemo IP adresu
max_retries = 100
number_of_retries = 0
# REFRESH 
instance.reload()
while instance.public_ip_address is None  and number_of_retries < max_retries:
    print("Address not yet available, waiting 5 seconds before trying again")
    time.sleep(5)
    number_of_retries += 1
    instance.reload()


print(f"It's address is {instance.public_ip_address}")


#eip = ec2.resource("eipalloc-1fb05d16")
#eip.associate (instances[0].instance_id)

# startuejemo instancu 
# sacekamo da ona dodje sebi
# i onda PREVEZEMO FIKSNU IP ADRESU SA STARE INSTANCE NA NOVU

# downtime-a
