from app.models.user import User
from app.models.account import Account
import unittest

class TestModels(unittest.TestCase):

    def setUp(self):
        self.user = User(id=1, username='testuser', balance=1000)
        self.account = Account(account_id=1, user_id=self.user.id, balance=1000)

    def test_user_initialization(self):
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.balance, 1000)

    def test_account_initialization(self):
        self.assertEqual(self.account.account_id, 1)
        self.assertEqual(self.account.user_id, self.user.id)
        self.assertEqual(self.account.balance, 1000)

    def test_user_balance_update(self):
        self.user.balance -= 200
        self.assertEqual(self.user.balance, 800)

    def test_account_balance_update(self):
        self.account.balance -= 300
        self.assertEqual(self.account.balance, 700)

if __name__ == '__main__':
    unittest.main()