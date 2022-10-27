#!/usr/bin/python3
from models.amenity import Amenity
import unittest

class TestAmenityClass(unittest.TestCase):

    def test_amenity_name(self):
        """test to check user name"""
        p1 = Amenity()
        self.assertEqual(type(p1.id), str)
        self.assertTrue(hasattr(p1, "name"))

if __name__ == "__main__":
    unittest.main()
