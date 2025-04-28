import json
import boto3
from utils.config_loader import load_credentials

def main():
    # Load AWS credentials from the configuration file
    credentials = load_credentials()
    
    # Initialize a session using the loaded credentials
    session = boto3.Session(
        aws_access_key_id=credentials['access_key'],
        aws_secret_access_key=credentials['secret_key'],
        region_name=credentials['region']
    )
    
    # Example of initializing EC2 service
    ec2_service = session.resource('ec2')
    
    # You can add more logic here to interact with AWS services

if __name__ == "__main__":
    main()