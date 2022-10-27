#!/usr/bin/python3

from models.user import User
import unittest

class TestUserClass(unittest.TestCase):

    def test_user_email(self):
        """Tests email for User"""
        u1 = User()
        self.assertEqual(type(u1.email), str)
        self.assertTrue(hasattr(u1, "email"))

    def test_user_password(self):
        """test to check user password"""
        User_1 = User()
        self.assertEqual(type(User_1.password), str)
        self.assertTrue(hasattr(User_1, "password"))
        
    def test_user_first_name(self):
        """test to check user first name"""
        User_1 = User()
        self.assertEqual(type(User_1.first_name), str)
        self.assertTrue(hasattr(User_1, "first_name"))

    def test_user_last_name(self):
        """test to check user last_name"""
        User_1 = User()
        self.assertEqual(type(User_1.last_name), str)
        self.assertTrue(hasattr(User_1, "last_name"))

if __name__ == "__main__":
    unittest.main()
