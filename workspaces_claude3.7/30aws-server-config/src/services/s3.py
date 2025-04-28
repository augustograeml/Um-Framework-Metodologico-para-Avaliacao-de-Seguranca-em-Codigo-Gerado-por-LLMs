class S3Service:
    def __init__(self, boto3_session):
        self.s3 = boto3_session.resource('s3')

    def upload_file(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = file_name
        self.s3.Bucket(bucket).upload_file(file_name, object_name)

    def download_file(self, bucket, object_name, file_name):
        self.s3.Bucket(bucket).download_file(object_name, file_name)

    def list_files(self, bucket):
        return [obj.key for obj in self.s3.Bucket(bucket).objects.all()]

    def delete_file(self, bucket, object_name):
        self.s3.Object(bucket, object_name).delete()