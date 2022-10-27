#!/usr/bin/python3

from models.city import City
import unittest

class TestCityClass(unittest.TestCase):
	
	def test_city_name(self):
		"""test to check user name"""
		User_1 = City()
		self.assertEqual(type(User_1.id), str)
		self.assertTrue(hasattr(User_1, "name"))

	def test_City_state_id(self):
		'''Tests state_id for City'''
		c1 = City()
		self.assertTrue(hasattr(c1, "state_id"))
		self.assertEqual(type(c1.state_id), str)

if __name__ == "__main__":
	unittest.main()
