import unittest
from src.models.data_model import DataModel

class TestDataModel(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Sample Name",
            "age": 30,
            "email": "sample@example.com"
        }
        self.data_model = DataModel(**self.data)

    def test_data_model_initialization(self):
        self.assertEqual(self.data_model.name, self.data["name"])
        self.assertEqual(self.data_model.age, self.data["age"])
        self.assertEqual(self.data_model.email, self.data["email"])

    def test_data_model_manipulation(self):
        new_name = "New Name"
        self.data_model.name = new_name
        self.assertEqual(self.data_model.name, new_name)

    def test_data_model_repr(self):
        expected_repr = f"DataModel(name={self.data['name']}, age={self.data['age']}, email={self.data['email']})"
        self.assertEqual(repr(self.data_model), expected_repr)

if __name__ == '__main__':
    unittest.main()