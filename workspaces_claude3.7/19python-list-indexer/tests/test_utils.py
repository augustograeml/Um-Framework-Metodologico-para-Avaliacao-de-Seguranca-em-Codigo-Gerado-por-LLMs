import unittest
from src.utils import get_item_from_list, validate_index

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    def test_get_item_from_list_valid_index(self):
        self.assertEqual(get_item_from_list(self.test_list, 1), 'banana')

    def test_get_item_from_list_invalid_index(self):
        self.assertIsNone(get_item_from_list(self.test_list, 10))

    def test_validate_index_valid(self):
        self.assertTrue(validate_index(2, self.test_list))

    def test_validate_index_invalid_negative(self):
        self.assertFalse(validate_index(-1, self.test_list))

    def test_validate_index_invalid_out_of_bounds(self):
        self.assertFalse(validate_index(5, self.test_list))

if __name__ == '__main__':
    unittest.main()