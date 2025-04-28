class RDSService:
    def __init__(self, boto3_session):
        self.rds_client = boto3_session.client('rds')

    def create_db_instance(self, db_instance_identifier, db_instance_class, engine, master_username, master_user_password):
        response = self.rds_client.create_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            DBInstanceClass=db_instance_class,
            Engine=engine,
            MasterUsername=master_username,
            MasterUserPassword=master_user_password,
            AllocatedStorage=20,
            StorageType='gp2',
            MultiAZ=False,
            PubliclyAccessible=True
        )
        return response

    def delete_db_instance(self, db_instance_identifier, skip_final_snapshot=True):
        response = self.rds_client.delete_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            SkipFinalSnapshot=skip_final_snapshot
        )
        return response

    def describe_db_instances(self):
        response = self.rds_client.describe_db_instances()
        return response['DBInstances']