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