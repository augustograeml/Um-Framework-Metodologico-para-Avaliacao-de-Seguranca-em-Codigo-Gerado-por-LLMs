import unittest
from unittest.mock import patch
from src.main import ping_ip

class TestMain(unittest.TestCase):

    @patch('src.ping_utils.ping_ip')
    def test_ping_valid_ip(self, mock_ping):
        mock_ping.return_value = "Ping successful"
        result = ping_ip("192.168.1.1")
        self.assertEqual(result, "Ping successful")
        mock_ping.assert_called_once_with("192.168.1.1")

    @patch('src.ping_utils.ping_ip')
    def test_ping_invalid_ip(self, mock_ping):
        mock_ping.side_effect = Exception("Invalid IP address")
        with self.assertRaises(Exception) as context:
            ping_ip("999.999.999.999")
        self.assertEqual(str(context.exception), "Invalid IP address")
        mock_ping.assert_called_once_with("999.999.999.999")

if __name__ == '__main__':
    unittest.main()