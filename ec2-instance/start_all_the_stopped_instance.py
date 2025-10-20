import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Step 1: Get all stopped instances
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
)

# Collect all instance IDs
stopped_instance_ids = [
    instance['InstanceId']
    for reservation in response['Reservations']
    for instance in reservation['Instances']
]

if not stopped_instance_ids:
    print("ℹ️ No stopped instances found.")
else:
    print(f"▶️ Starting instances: {stopped_instance_ids}")
    
    # Step 2: Start instances
    ec2.start_instances(InstanceIds=stopped_instance_ids)
    print("✅ Start request sent for all stopped instances.")
