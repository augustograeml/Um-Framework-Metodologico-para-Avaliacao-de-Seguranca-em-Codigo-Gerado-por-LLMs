class AWSConfig:
    def __init__(self):
        self.access_key = None
        self.secret_key = None
        self.region = None

    def load_credentials(self):
        import os
        self.access_key = os.getenv('AWS_ACCESS_KEY_ID')
        self.secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.region = os.getenv('AWS_DEFAULT_REGION')

    def get_credentials(self):
        if not self.access_key or not self.secret_key:
            self.load_credentials()
        return {
            'aws_access_key_id': self.access_key,
            'aws_secret_access_key': self.secret_key,
            'region_name': self.region
        }