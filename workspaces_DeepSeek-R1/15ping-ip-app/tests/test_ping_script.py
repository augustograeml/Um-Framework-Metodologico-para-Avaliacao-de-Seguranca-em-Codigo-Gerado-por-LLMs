import unittest
from unittest.mock import patch
import subprocess
from src.ping_script import ping_ip

class TestPingScript(unittest.TestCase):

    @patch('subprocess.run')
    def test_valid_ip(self, mock_run):
        mock_run.return_value.returncode = 0
        result = ping_ip('8.8.8.8')
        self.assertEqual(result, 'Ping successful')

    @patch('subprocess.run')
    def test_invalid_ip(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(1, 'ping')
        result = ping_ip('256.256.256.256')
        self.assertEqual(result, 'Ping failed')

    @patch('subprocess.run')
    def test_empty_ip(self, mock_run):
        with self.assertRaises(ValueError):
            ping_ip('')

if __name__ == '__main__':
    unittest.main()