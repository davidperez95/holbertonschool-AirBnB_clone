#!/usr/bin/python3
from models.amenity import Amenity
import unittest

class TestAmenityClass(unittest.TestCase):

    def test_amenity_name(self):
        """test to check user name"""
        c1 = Amenity()
        self.assertTrue(hasattr(c1, "name"))
        self.assertEqual(type(c1.name), str)

if __name__ == "__main__":
    unittest.main()
