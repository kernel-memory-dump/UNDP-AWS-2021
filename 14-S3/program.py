import boto3


s3_client = boto3.client("s3",
   aws_access_key_id='',
    aws_secret_access_key='')
file_za_upload = open('example.txt', 'r')
content = file_za_upload.read()
response = s3_client.put_object(
    Bucket="sebastian-novi-sad-2021-test",
    Key="example222.txt",
    Body=content
)


print(str(response))