class EC2Service:
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client

    def start_instance(self, instance_id):
        response = self.ec2_client.start_instances(InstanceIds=[instance_id])
        return response

    def stop_instance(self, instance_id):
        response = self.ec2_client.stop_instances(InstanceIds=[instance_id])
        return response

    def get_instance_status(self, instance_id):
        response = self.ec2_client.describe_instance_status(InstanceIds=[instance_id])
        return response['InstanceStatuses'][0] if response['InstanceStatuses'] else None