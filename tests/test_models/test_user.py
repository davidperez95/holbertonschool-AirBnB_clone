#!/usr/bin/python3

from models.user import User
from models.base_model import BaseModel
import unittest

class TestUserClass(unittest.TestCase):

    def test_user_email(self):
        """Tests email for User"""
        u1 = User()
        self.assertEqual(type(u1.email), str)
        self.assertTrue(hasattr(u1, "email"))
