class EC2Service:
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client

    def create_instance(self, image_id, instance_type, key_name, security_group_ids):
        response = self.ec2_client.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            MinCount=1,
            MaxCount=1
        )
        return response['Instances'][0]['InstanceId']

    def start_instance(self, instance_id):
        response = self.ec2_client.start_instances(InstanceIds=[instance_id])
        return response

    def stop_instance(self, instance_id):
        response = self.ec2_client.stop_instances(InstanceIds=[instance_id])
        return response

    def terminate_instance(self, instance_id):
        response = self.ec2_client.terminate_instances(InstanceIds=[instance_id])
        return response