#!/usr/bin/python3

from models.place import Place
import unittest

class TestPlaceClass(unittest.TestCase):

    def test_place_city_id(self):
        '''Tests if has id attribute'''
        p1 = Place()
        self.assertEqual(type(p1.id), str)
        self.assertTrue(hasattr(p1, "city_id"))

    def test_place_user_id(self):
        '''Tests if has user_id attribute'''
        p1 = Place()
        self.assertEqual(type(p1.id), str)
        self.assertTrue(hasattr(p1, "user_id"))

    def test_place_name(self):
        """test to check user name"""
        p1 = Place()
        self.assertEqual(type(p1.id), str)
        self.assertTrue(hasattr(p1, "name"))

    def test_place_description(self):
        '''Tests description for place'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "description"))
        self.assertEqual(type(p1.description), str)
    
    def test_place_number_rooms(self):
        '''Tests number of rooms for place'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertEqual(type(p1.number_rooms), int)

    def test_place_number_bathrooms(self):
        '''Tests number of bathrooms for place'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "number_bathrooms"))
        self.assertEqual(type(p1.number_bathrooms), int)

    def test_place_max_guest(self):
        '''Tests max number of guests'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertEqual(type(p1.max_guest), int)

    def test_place_price_by_night(self):
        '''Tests price by night'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertEqual(type(p1.price_by_night), int)

    def test_place_latitude(self):
        '''Tests latitude'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "latitude"))
        self.assertEqual(type(p1.latitude), float)

    def test_place_longitude(self):
        '''Tests longitude'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "longitude"))
        self.assertEqual(type(p1.longitude), float)

    def test_amenity_ids(self):
        '''Tests amenity ids'''
        p1 = Place()
        self.assertTrue(hasattr(p1, "amenity_ids"))
        self.assertEqual(type(p1.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
