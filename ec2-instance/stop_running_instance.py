import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Step 1: Get all running instances
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# Collect all instance IDs
running_instance_ids = [
    instance['InstanceId']
    for reservation in response['Reservations']
    for instance in reservation['Instances']
]

if not running_instance_ids:
    print("ℹ️ No running instances found.")
else:
    print(f"⏸️ Stopping instances: {running_instance_ids}")
    
    # Step 2: Stop instances
    ec2.stop_instances(InstanceIds=running_instance_ids)
    print("✅ Stop request sent for all running instances.")
