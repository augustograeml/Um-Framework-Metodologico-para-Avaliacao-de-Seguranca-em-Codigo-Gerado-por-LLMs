import unittest
from src.converter.object_mapper import ObjectMapper
from src.models.data_models import YourDataModel  # Replace with your actual data model

class TestObjectMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = ObjectMapper()

    def test_map_to_object(self):
        sample_data = {
            "attribute1": "value1",
            "attribute2": "value2"
        }
        obj = self.mapper.map_to_object(sample_data, YourDataModel)
        
        self.assertIsInstance(obj, YourDataModel)
        self.assertEqual(obj.attribute1, "value1")
        self.assertEqual(obj.attribute2, "value2")

    def test_map_to_object_with_missing_attributes(self):
        sample_data = {
            "attribute1": "value1"
        }
        obj = self.mapper.map_to_object(sample_data, YourDataModel)
        
        self.assertIsInstance(obj, YourDataModel)
        self.assertEqual(obj.attribute1, "value1")
        self.assertIsNone(obj.attribute2)  # Assuming attribute2 is optional

if __name__ == '__main__':
    unittest.main()