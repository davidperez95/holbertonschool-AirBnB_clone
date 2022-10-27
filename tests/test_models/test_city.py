#!/usr/bin/python3

from models.city import City
import unittest

class TestUserClass(unittest.TestCase):
	
	def test_city_name(self):
		"""test to check user name"""
		User_1 = City()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "name"))

if __name__ == "__main__":
	unittest.main()
