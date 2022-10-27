#!/usr/bin/python3

from models.state import State
import unittest

class TestUserClass(unittest.TestCase):

    def test_state_name(self):
        """test to check user name"""
        User_1 = State()
        self.assertEqual(type(User_1.name), str)
        self.assertTrue(hasattr(User_1, "name"))

if __name__ == "__main__":
    unittest.main()
