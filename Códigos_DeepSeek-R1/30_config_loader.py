def load_credentials(file_path='config/aws_credentials.json'):
    import json

    with open(file_path, 'r') as file:
        credentials = json.load(file)

    return credentials