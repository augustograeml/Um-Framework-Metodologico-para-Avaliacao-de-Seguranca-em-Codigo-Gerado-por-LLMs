import unittest
from config_system.utils import serialize, deserialize

class TestUtils(unittest.TestCase):

    def test_serialize(self):
        data = {'key': 'value'}
        serialized_data = serialize(data)
        self.assertIsInstance(serialized_data, bytes)

    def test_deserialize(self):
        data = {'key': 'value'}
        serialized_data = serialize(data)
        deserialized_data = deserialize(serialized_data)
        self.assertEqual(data, deserialized_data)

    def test_deserialize_invalid(self):
        with self.assertRaises(ValueError):
            deserialize(b'invalid serialized data')