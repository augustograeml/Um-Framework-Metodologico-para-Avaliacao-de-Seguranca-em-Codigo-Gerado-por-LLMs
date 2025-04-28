import os
import boto3
from src.config.credentials import load_credentials
from src.utils.logger import setup_logging

def main():
    setup_logging()
    
    # Load AWS credentials
    aws_access_key, aws_secret_key, region = load_credentials()
    
    # Initialize AWS services
    ec2 = boto3.resource('ec2', 
                         aws_access_key_id=aws_access_key, 
                         aws_secret_access_key=aws_secret_key, 
                         region_name=region)
    
    # Example: Print available EC2 instances
    instances = ec2.instances.all()
    for instance in instances:
        print(f'Instance ID: {instance.id}, State: {instance.state["Name"]}')

if __name__ == "__main__":
    main()