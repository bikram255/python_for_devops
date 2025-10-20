import boto3

# Initialize EC2 and IAM clients
ec2 = boto3.client('ec2')
iam = boto3.client('iam')

# Step 1: Create or get IAM role
role_name = 'kops_role'

try:
    iam.get_role(RoleName=role_name)
    print(f"IAM Role '{role_name}' already exists.")
except iam.exceptions.NoSuchEntityException:
    print(f"Creating IAM Role: {role_name}")
    assume_role_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "ec2.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }

    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )

    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'  # Example policy
    )

# Step 2: Create Instance Profile (if not exists)
profile_name = role_name + '-InstanceProfile'

try:
    iam.get_instance_profile(InstanceProfileName=profile_name)
    print(f"Instance profile '{profile_name}' already exists.")
except iam.exceptions.NoSuchEntityException:
    print(f"Creating instance profile: {profile_name}")
    iam.create_instance_profile(InstanceProfileName=profile_name)
    iam.add_role_to_instance_profile(
        InstanceProfileName=profile_name,
        RoleName=role_name
    )

# Step 3: Attach instance profile to an existing EC2 instance
instance_id = 'i-0f40128fe41204796'  # Replace with your instance ID

response = ec2.associate_iam_instance_profile(
    IamInstanceProfile={'Name': profile_name},
    InstanceId=instance_id
)

print("IAM role attached successfully:", response)
