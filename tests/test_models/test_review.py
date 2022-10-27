#!/usr/bin/python3

from models.review import Review
import unittest

class TestReviewClass(unittest.TestCase):

    def test_review_place_and_user_id(self):
        """test to check user id"""
        User_1 = Review()
        self.assertEqual(type(User_1.id), str)
        self.assertTrue(hasattr(User_1, "id"))
    
    def test_review_text(self):
        """test to check text of review"""
        User_1 = Review()
        self.assertEqual(type(User_1.text), str)
        self.assertTrue(hasattr(User_1, "text"))

if __name__ == "__main__":
    unittest.main()
