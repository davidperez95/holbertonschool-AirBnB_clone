#!/usr/bin/python3
from models.amenity import Amenity
import unittest

class TestAmenityClass(unittest.TestCase):

    def test_amenity_name(self):
        """test to check user name"""
        User_1 = Amenity()
        self.assertEqual(type(User_1.id), str)
        self.assertTrue(hasattr(User_1, "name"))

if __name__ == "__main__":
    unittest.main()
