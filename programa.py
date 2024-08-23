import boto3
client = boto3.client("s3" , "us-east-1")
response = client.list:buckets()
print(response)