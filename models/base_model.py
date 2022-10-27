#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""Module BaseModel"""


class BaseModel:
    """
    Class BaseModel that create a instance with
    attributes id, created and update
    """
    def __init__(self, *args, **kwargs):
        """Instance constructor for the Base Model class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    dt_obj = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dt_obj)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method return a string class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method update of the instance"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This method modify and convert all attributes to
        string and return dictionaty
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        return new_dict
