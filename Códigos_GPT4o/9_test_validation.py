import unittest
from app.utils.validation import is_positive_amount, is_valid_user_id

class TestValidation(unittest.TestCase):

    def test_is_positive_amount(self):
        self.assertTrue(is_positive_amount(10))
        self.assertTrue(is_positive_amount(0.01))
        self.assertFalse(is_positive_amount(-5))
        self.assertFalse(is_positive_amount(0))

    def test_is_valid_user_id(self):
        valid_user_ids = ['user1', 'user2', 'user3']
        self.assertTrue(is_valid_user_id('user1', valid_user_ids))
        self.assertTrue(is_valid_user_id('user2', valid_user_ids))
        self.assertFalse(is_valid_user_id('user4', valid_user_ids))