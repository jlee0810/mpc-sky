import boto3
import os


def create_key_pair(ec2_client, key_name):
    response = ec2_client.create_key_pair(KeyName=key_name)
    private_key = response["KeyMaterial"]

    key_path = f"{key_name}.pem"
    with open(key_path, "w") as key_file:
        key_file.write(private_key)

    os.chmod(key_path, 0o400)

    return key_path


def create_security_group(ec2_client, group_name, description, vpc_id):
    response = ec2_client.create_security_group(
        GroupName=group_name, Description=description, VpcId=vpc_id
    )
    security_group_id = response["GroupId"]

    ec2_client.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22,
                "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
            }
        ],
    )

    return security_group_id


user_data_script = """#!/bin/bash
sudo apt update -y
sudo apt install -y python3

# Your Python script
echo "
print('Hello from EC2 instance')
" > /home/ubuntu/your_script.py

# Run the Python script and save the output
python3 /home/ubuntu/your_script.py > /home/ubuntu/output.txt 2>&1
"""

ec2_client = boto3.client("ec2")
ec2_resource = boto3.resource("ec2")

key_name = "my-key-pair"
key_path = create_key_pair(ec2_client, key_name)
print(f"Key pair created and saved to {key_path}")

vpcs = ec2_client.describe_vpcs()
vpc_id = vpcs["Vpcs"][0]["VpcId"]

security_group_name = "my-security-group"
security_group_description = "Security group for SSH access"
security_group_id = create_security_group(
    ec2_client, security_group_name, security_group_description, vpc_id
)
print(f"Security group created with ID: {security_group_id}")

instances = ec2_resource.create_instances(
    ImageId="ami-09d56f8956ab235b3",  # Replace with the AMI ID for Ubuntu
    MinCount=1,
    MaxCount=1,
    InstanceType="t2.micro",
    KeyName=key_name,
    SecurityGroupIds=[security_group_id],
    UserData=user_data_script,
)

instance = instances[0]
print("Waiting for instance to enter running state...")
instance.wait_until_running()

instance.reload()
print("Instance created with ID:", instance.id)
print("Public DNS:", instance.public_dns_name)
