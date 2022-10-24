#!/usr/bin/python3
import unittest
from models import base_model
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestsCase):
    """Tests for the base class"""
    def TestSave(self):
        """Test of the save method"""
        