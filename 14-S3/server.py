import boto3


s3_client = boto3.client("s3",
   aws_access_key_id='',
    aws_secret_access_key='')
file_za_upload = open('za-upload.txt', 'r')
content = file_za_upload.read()
response = s3_client.put_object(
    Bucket="sebastian-undp2021",
    Key="david/za-upload.txt",
    Body=content
)

response = s3_client.delete_object(
    Bucket="sebastian-undp2021",
    Key="david/*",
)


print(str(response))
