import unittest
from app.models.account import Account
from app.services.transfer_service import TransferService

class TestTransferService(unittest.TestCase):

    def setUp(self):
        self.sender = Account(user_id='user1', balance=1000)
        self.receiver = Account(user_id='user2', balance=500)
        self.transfer_service = TransferService()

    def test_transfer_funds_success(self):
        result = self.transfer_service.transfer_funds(self.sender, self.receiver.user_id, 200)
        self.assertTrue(result)
        self.assertEqual(self.sender.balance, 800)
        self.assertEqual(self.receiver.balance, 700)

    def test_transfer_funds_insufficient_balance(self):
        result = self.transfer_service.transfer_funds(self.sender, self.receiver.user_id, 1200)
        self.assertFalse(result)
        self.assertEqual(self.sender.balance, 1000)
        self.assertEqual(self.receiver.balance, 500)

    def test_transfer_funds_invalid_user(self):
        result = self.transfer_service.transfer_funds(self.sender, 'invalid_user', 200)
        self.assertFalse(result)
        self.assertEqual(self.sender.balance, 1000)
        self.assertEqual(self.receiver.balance, 500)

if __name__ == '__main__':
    unittest.main()