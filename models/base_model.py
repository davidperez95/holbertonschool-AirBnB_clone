#!/usr/bin/python3
import uuid
import datetime
"""Module BaseModel"""


class BaseModel:
    """
    Class BaseModel that create a instance with
    attributes id, created and update
    """
    def __init__(self, *args, **kwargs):
        """Instance constructor for the Base Model class"""
        if len(kwargs) <= 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = kwargs["created_at"]
            if "udpated_at" in kwargs:
                self.updated_at = kwargs["updated_at"]

    def __str__(self):
        """This method return a string class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """This method update of the instance"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        This method modify and convert all attributes to
        string and return dictionaty
        """
        dic = self.__dict__.copy()
        dic["__class__"] = __class__.__name__
        dic["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        dic["created_at"] = datetime.datetime.isoformat(self.created_at)
        return dic
