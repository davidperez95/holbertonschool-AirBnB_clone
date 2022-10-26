#!/usr/bin/python3
"""Module contains the FileStorage class"""
from models.base_model import BaseModel
import json


class FileStorage():
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    
    def __init__(self):
        """pass"""
        pass

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_obj = obj.__class__.__name__ + "." + obj.id
        self.__objects[key_obj] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                file_dict = json.load(file)
                for key, value in file_dict.items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except:
            pass
