#!/usr/bin/python3
"""Module contains the FileStorage class"""
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
        for key in self.__objects:
            json_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                self.__objects = json.load(file)
                """
                for key, value in (json.load(file)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
                """
        except:
            pass


"""
new_obj1 = {'my_number': 89, 'updated_at': 'datetime.datetime(2017, 9, 28, 21, 7, 25, 47381)', 'created_at': 'datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)', 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
new_obj2 = {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': 'datetime.datetime(2017, 9, 28, 21, 7, 51, 973308)', 'my_number': 89, 'created_at': 'datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)'}
new_file = FileStorage()
new_file.new(new_obj1)
new_file.new(new_obj2)
print(new_file.all())
print("before reload")
new_file.save()
new_file.reload()
print()
print(new_file.all())
print("after reload")
"""