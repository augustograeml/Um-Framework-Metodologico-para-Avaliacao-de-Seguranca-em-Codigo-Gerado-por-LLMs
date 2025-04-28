def validate_aws_credentials(access_key, secret_key):
    if not access_key or not secret_key:
        return False
    # Additional validation logic can be added here
    return True

def is_valid_region(region):
    valid_regions = [
        'us-east-1', 'us-west-1', 'us-west-2',
        'eu-central-1', 'eu-west-1', 'eu-west-2',
        'ap-south-1', 'ap-northeast-1', 'ap-northeast-2',
        'sa-east-1', 'ca-central-1'
    ]
    return region in valid_regions