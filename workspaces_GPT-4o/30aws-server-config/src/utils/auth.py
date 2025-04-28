def get_aws_credentials():
    import os

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    if not aws_access_key_id or not aws_secret_access_key:
        raise ValueError("AWS credentials are not set in environment variables.")

    return aws_access_key_id, aws_secret_access_key