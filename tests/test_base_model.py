#!/usr/bin/python3
import unittest
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestsCase):
    """Tests for the base class"""
    
    def TestSave(self):
        """Test of the save method"""
        my_BaseModel = BaseModel()
        my_1BaseModel = my_BaseModel.updated_at
        my_BaseModel.save()
        my_2BaseModel = my_BaseModel.updated_at
        self.assertNotEqual(my_1BaseModel, my_2BaseModel)
