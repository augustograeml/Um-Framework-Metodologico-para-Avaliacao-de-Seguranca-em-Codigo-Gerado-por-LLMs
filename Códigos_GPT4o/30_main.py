from utils.auth import get_aws_credentials
from config.aws_config import AWSConfig
from services.ec2_service import EC2Service

def main():
    # Load AWS credentials
    aws_access_key, aws_secret_key = get_aws_credentials()
    
    # Initialize AWS configuration
    aws_config = AWSConfig(aws_access_key, aws_secret_key)
    
    # Initialize EC2 service
    ec2_service = EC2Service(aws_config)
    
    # Example usage: Create an EC2 instance
    instance_id = ec2_service.create_instance()
    print(f"EC2 Instance created with ID: {instance_id}")

if __name__ == "__main__":
    main()