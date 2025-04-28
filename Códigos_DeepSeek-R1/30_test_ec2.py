import unittest
from unittest.mock import patch, MagicMock
from aws_services.ec2 import EC2Service

class TestEC2Service(unittest.TestCase):

    @patch('aws_services.ec2.boto3.client')
    def test_start_instance(self, mock_boto_client):
        mock_ec2 = MagicMock()
        mock_boto_client.return_value = mock_ec2
        ec2_service = EC2Service()

        instance_id = 'i-1234567890abcdef0'
        ec2_service.start_instance(instance_id)

        mock_ec2.start_instances.assert_called_once_with(InstanceIds=[instance_id])

    @patch('aws_services.ec2.boto3.client')
    def test_stop_instance(self, mock_boto_client):
        mock_ec2 = MagicMock()
        mock_boto_client.return_value = mock_ec2
        ec2_service = EC2Service()

        instance_id = 'i-1234567890abcdef0'
        ec2_service.stop_instance(instance_id)

        mock_ec2.stop_instances.assert_called_once_with(InstanceIds=[instance_id])

    @patch('aws_services.ec2.boto3.client')
    def test_get_instance_status(self, mock_boto_client):
        mock_ec2 = MagicMock()
        mock_boto_client.return_value = mock_ec2
        ec2_service = EC2Service()

        instance_id = 'i-1234567890abcdef0'
        mock_ec2.describe_instance_status.return_value = {
            'InstanceStatuses': [{'InstanceId': instance_id, 'InstanceState': {'Name': 'running'}}]
        }

        status = ec2_service.get_instance_status(instance_id)

        self.assertEqual(status, 'running')
        mock_ec2.describe_instance_status.assert_called_once_with(InstanceIds=[instance_id])

if __name__ == '__main__':
    unittest.main()