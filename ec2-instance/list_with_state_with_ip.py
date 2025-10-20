import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

print("---- EC2 Instance Details ----")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        state = instance['State']['Name']
        public_ip = instance.get('PublicIpAddress', 'N/A')
        private_ip = instance.get('PrivateIpAddress', 'N/A')
        key_name = instance.get('KeyName', 'N/A')
        placement = instance['Placement']['AvailabilityZone']

        # Fetch Name tag if present
        name = 'N/A'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']

        print(f"\n🖥️ Name: {name}")
        print(f"Instance ID: {instance_id}")
        print(f"Type: {instance_type}")
        print(f"State: {state}")
        print(f"Public IP: {public_ip}")
        print(f"Private IP: {private_ip}")
        print(f"SSH Key Pair : {key_name}")
        print(f"Availability Zone : {placement}")
        print("-----------------------------")
