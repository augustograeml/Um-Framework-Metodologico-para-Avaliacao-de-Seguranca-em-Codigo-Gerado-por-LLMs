import unittest
from src.main import get_item_from_list

class TestMain(unittest.TestCase):
    def test_valid_index(self):
        self.assertEqual(get_item_from_list(1), "item2")

    def test_index_out_of_bounds(self):
        self.assertEqual(get_item_from_list(10), "Index out of bounds")

    def test_negative_index(self):
        self.assertEqual(get_item_from_list(-1), "Index out of bounds")

if __name__ == '__main__':
    unittest.main()