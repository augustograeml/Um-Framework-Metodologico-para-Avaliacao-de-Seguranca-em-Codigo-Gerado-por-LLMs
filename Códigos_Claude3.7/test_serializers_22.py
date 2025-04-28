import unittest
from config_system.serializers.json_serializer import JsonSerializer
from config_system.serializers.yaml_serializer import YamlSerializer

class TestJsonSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = JsonSerializer()

    def test_serialize(self):
        data = {"key": "value"}
        expected = '{"key": "value"}'
        result = self.serializer.serialize(data)
        self.assertEqual(result, expected)

    def test_deserialize(self):
        json_data = '{"key": "value"}'
        expected = {"key": "value"}
        result = self.serializer.deserialize(json_data)
        self.assertEqual(result, expected)

class TestYamlSerializer(unittest.TestCase):
    def setUp(self):
        self.serializer = YamlSerializer()

    def test_serialize(self):
        data = {"key": "value"}
        expected = "key: value\n"
        result = self.serializer.serialize(data)
        self.assertEqual(result, expected)

    def test_deserialize(self):
        yaml_data = "key: value\n"
        expected = {"key": "value"}
        result = self.serializer.deserialize(yaml_data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()