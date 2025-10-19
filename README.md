# python_for_devops

# Code to Create a s3 bucket in aws
import boto3

region = 'ap-south-1'
client = boto3.client('s3')
response = client.create_bucket(
    Bucket='testbucketbikram2025',
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)
print(response)




# Code to Delete a s3 bucket in aws
import boto3

region = 'ap-south-1'
client = boto3.client('s3')
response = client.delete_bucket(
    Bucket='testbucketbikram2025',
)
print(response)