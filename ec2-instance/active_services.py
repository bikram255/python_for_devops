import boto3

# Initialize clients
ec2 = boto3.client('ec2')
rds = boto3.client('rds')
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')
route53 = boto3.client('route53')

print("========== ACTIVE AWS RESOURCES ==========")

# 1️⃣ EC2 Instances (running)
print("\n--- EC2 Instances (Running) ---")
ec2_response = ec2.describe_instances(Filters=[{'Name':'instance-state-name','Values':['running']}])
for reservation in ec2_response['Reservations']:
    for instance in reservation['Instances']:
        name = 'N/A'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                name = tag['Value']
        print(f"Name: {name}, ID: {instance['InstanceId']}, Type: {instance['InstanceType']}, Public IP: {instance.get('PublicIpAddress','N/A')}")

# 2️⃣ RDS Instances (available)
print("\n--- RDS Instances (Available) ---")
rds_response = rds.describe_db_instances()
for db in rds_response['DBInstances']:
    if db['DBInstanceStatus'] == 'available':
        print(f"DB: {db['DBInstanceIdentifier']}, Engine: {db['Engine']}, Class: {db['DBInstanceClass']}")

# 3️⃣ S3 Buckets
print("\n--- S3 Buckets ---")
s3_response = s3.list_buckets()
for bucket in s3_response['Buckets']:
    print(f"Bucket Name: {bucket['Name']}")

# 4️⃣ Lambda Functions
print("\n--- Lambda Functions ---")
lambda_response = lambda_client.list_functions()
for function in lambda_response['Functions']:
    print(f"Function Name: {function['FunctionName']}, Runtime: {function['Runtime']}, Last Modified: {function['LastModified']}")

# 5️⃣ EBS Volumes (in-use)
print("\n--- EBS Volumes (In-use) ---")
volumes = ec2.describe_volumes(Filters=[{'Name':'status','Values':['in-use']}])
for vol in volumes['Volumes']:
    print(f"Volume ID: {vol['VolumeId']}, Size: {vol['Size']} GB, AZ: {vol['AvailabilityZone']}")

# 6️⃣ Route 53 Hosted Zones
print("\n--- Route 53 Hosted Zones ---")
zones = route53.list_hosted_zones()
for zone in zones['HostedZones']:
    print(f"Zone Name: {zone['Name']}, ID: {zone['Id']}, Record Count: {zone['ResourceRecordSetCount']}")
