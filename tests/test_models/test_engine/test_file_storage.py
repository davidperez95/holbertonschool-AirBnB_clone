#!/usr/bin/python3
"""
Instantiating Users
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import unittest


class TestFileStorageClass(unittest.TestCase):
    """class test"""

    @classmethod
    def setUpClass(cls):
        """
        Setting up class attributes
        """

    def test_all_storage(self):
        """ Test method all"""
        obj = models.storage.all()
        self.assertIsInstance(obj, dict)

    def test_new_storage(self):
        """Test method new"""
        FS = FileStorage().all()
        self.assertEqual(type(FS), dict)

    def test_save_storage(self):
        """Test method save"""
        FS = FileStorage()
        B_M = BaseModel()
        FS.new(B_M)
        FS.save()
        with open("file.json", "r", encoding='utf-8') as r:
            Json_full = r.read()
            self.assertTrue(f"BaseModel.{B_M.id}" in Json_full)

    def test_reload_storage(self):
        """
        Method that tests:
            if file storage was documented
            and checks reload() method exists
        """
        self.storage = FileStorage()
        MyModel = BaseModel()
        self.storage.save()
        self.storage.reload()
        key = "BaseModel.{}".format(MyModel.id)
        ob_dict = self.storage.all()
        self.assertFalse(ob_dict[key] is MyModel)

if __name__ == "__main__":
    unittest.main()
