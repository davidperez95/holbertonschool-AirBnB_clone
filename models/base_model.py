#!/usr/bin/python3
import uuid
import datetime
import models
"""Module BaseModel"""


class BaseModel:
    """
    Class BaseModel that create a instance with
    attributes id, created and update
    """
    def __init__(self, *args, **kwargs):
        """Instance constructor for the Base Model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "udpated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        models.storage.new(self)

    def __str__(self):
        """This method return a string class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

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
        new_dict["__class__"] = __class__.__name__
        new_dict["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        new_dict["created_at"] = datetime.datetime.isoformat(self.created_at)
        return new_dict
