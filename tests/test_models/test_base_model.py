#!/usr/bin/python3
import unittest
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the base class"""
    def test_save(self):
        """Test of the save method"""
        b = BaseModel()
        before = b.updated_at
        b.save()
        after = b.updated_at
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        """Test of the to_dict method"""
        x = BaseModel()
        new_dic = x.to_dict()
        self.assertTrue(type(new_dic) == dict)

    def test_self_id(self):
        """Test of the attribute id"""
        x = BaseModel()
        num = x.id
        self.assertTrue(type(num) == str)

    def test_created(self):
        """Test of the created_at method"""
        b = BaseModel()
        before = b.created_at
        b.save()
        after = b.created_at
        self.assertEqual(before, after)

    def test_str(self):
        """Test of the str method"""
        x = BaseModel()
        string = x.__str__()
        self.assertTrue(type(string) == str)
