import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Retrieve all instances
response = ec2.describe_instances()

# Loop through all reservations and instances
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
