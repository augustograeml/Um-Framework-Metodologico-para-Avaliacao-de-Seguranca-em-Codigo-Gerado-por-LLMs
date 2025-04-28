import unittest
from src.validators import validate_ip

class TestValidators(unittest.TestCase):

    def test_valid_ip(self):
        self.assertTrue(validate_ip("192.168.1.1"))
        self.assertTrue(validate_ip("255.255.255.255"))
        self.assertTrue(validate_ip("0.0.0.0"))

    def test_invalid_ip(self):
        self.assertFalse(validate_ip("256.256.256.256"))
        self.assertFalse(validate_ip("192.168.1"))
        self.assertFalse(validate_ip("192.168.1.1.1"))
        self.assertFalse(validate_ip("abc.def.ghi.jkl"))

if __name__ == '__main__':
    unittest.main()