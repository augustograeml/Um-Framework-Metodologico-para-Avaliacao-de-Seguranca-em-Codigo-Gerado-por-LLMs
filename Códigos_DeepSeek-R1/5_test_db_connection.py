import unittest
from database.db_connection import DbConnection

class TestDbConnection(unittest.TestCase):

    def setUp(self):
        self.db = DbConnection()

    def test_connect(self):
        self.assertTrue(self.db.connect())

    def test_close(self):
        self.db.connect()
        self.assertIsNone(self.db.close())

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()