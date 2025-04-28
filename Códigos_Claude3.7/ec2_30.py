class EC2Service:
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client

    def launch_instance(self, image_id, instance_type, key_name, security_group_ids):
        response = self.ec2_client.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            MinCount=1,
            MaxCount=1
        )
        return response['Instances'][0]['InstanceId']

    def stop_instance(self, instance_id):
        response = self.ec2_client.stop_instances(
            InstanceIds=[instance_id]
        )
        return response['StoppingInstances']

    def terminate_instance(self, instance_id):
        response = self.ec2_client.terminate_instances(
            InstanceIds=[instance_id]
        )
        return response['TerminatingInstances']

    def describe_instances(self):
        response = self.ec2_client.describe_instances()
        return response['Reservations']