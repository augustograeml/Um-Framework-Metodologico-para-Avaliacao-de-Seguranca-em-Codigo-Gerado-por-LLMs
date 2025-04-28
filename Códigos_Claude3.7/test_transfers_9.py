import unittest
from app.models.user import User
from app.models.account import Account
from app.services.transfer_service import TransferService

class TestTransferFunctionality(unittest.TestCase):

    def setUp(self):
        self.sender = User(id=1, username='sender', balance=100)
        self.receiver = User(id=2, username='receiver', balance=50)
        self.sender_account = Account(account_id=1, user_id=self.sender.id, balance=self.sender.balance)
        self.receiver_account = Account(account_id=2, user_id=self.receiver.id, balance=self.receiver.balance)
        self.transfer_service = TransferService()

    def test_successful_transfer(self):
        amount = 50
        result = self.transfer_service.transfer_funds(self.sender_account, self.receiver_account, amount)
        self.assertTrue(result)
        self.assertEqual(self.sender_account.balance, 50)
        self.assertEqual(self.receiver_account.balance, 100)

    def test_insufficient_balance(self):
        amount = 150
        result = self.transfer_service.transfer_funds(self.sender_account, self.receiver_account, amount)
        self.assertFalse(result)
        self.assertEqual(self.sender_account.balance, 100)
        self.assertEqual(self.receiver_account.balance, 50)

    def test_transfer_to_self(self):
        amount = 50
        result = self.transfer_service.transfer_funds(self.sender_account, self.sender_account, amount)
        self.assertFalse(result)
        self.assertEqual(self.sender_account.balance, 100)

if __name__ == '__main__':
    unittest.main()