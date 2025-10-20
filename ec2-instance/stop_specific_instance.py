import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Replace with your instance ID
instance_id = 'i-0123456789abcdef0'

# Stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

print(f"⏸️ Stop request sent for instance {instance_id}")
print(response)
