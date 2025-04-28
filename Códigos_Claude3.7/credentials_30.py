def load_credentials_from_env():
    import os

    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_session_token = os.getenv('AWS_SESSION_TOKEN')

    if not aws_access_key_id or not aws_secret_access_key:
        raise ValueError("AWS credentials not found in environment variables.")

    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'aws_session_token': aws_session_token
    }

def load_credentials_from_file(file_path):
    import configparser

    config = configparser.ConfigParser()
    config.read(file_path)

    try:
        aws_access_key_id = config['DEFAULT']['AWS_ACCESS_KEY_ID']
        aws_secret_access_key = config['DEFAULT']['AWS_SECRET_ACCESS_KEY']
        aws_session_token = config['DEFAULT'].get('AWS_SESSION_TOKEN', None)
    except KeyError as e:
        raise ValueError(f"Missing key in configuration file: {e}")

    return {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'aws_session_token': aws_session_token
    }