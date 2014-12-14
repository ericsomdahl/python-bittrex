__author__ = 'eric'

import unittest
from bittrex.bittrex import Bittrex

"""
Integration tests for the Bittrex API.
These will fail in the absence of an internet connection or if bittrex API goes down
"""


class TestBittrexPublicAPI(unittest.TestCase):
    def setUp(self):
        self.bittrex = Bittrex(None, None)

    def test_public_handles_none_key_or_secret(self):
        self.bittrex = Bittrex(None, None)
        # could call any public method here
        actual = self.bittrex.get_markets()
        self.assertTrue(actual['success'], "failed with None key and None secret")

        self.bittrex = Bittrex("123", None)
        actual = self.bittrex.get_markets()
        self.assertTrue(actual['success'], "failed with None secret")

        self.bittrex = Bittrex(None, "123")
        self.assertTrue(actual['success'], "failed with None key")

    def test_get_markets(self):
        actual = self.bittrex.get_markets()
        self.assertTrue(actual['success'], "get_markets failed")
        self.assertTrue(actual['message'] is not None, "message not present in response")
        self.assertTrue(actual['result'] is not None, "result not present in response")
        self.assertTrue(isinstance(actual['result'], list), "result is not a list")
        self.assertTrue(len(actual['result']) > 0, "result list is 0-length")

if __name__ == '__main__':
    unittest.main()

