#!/usr/bin/python3
"""
    File Storgae engine, Write a class FileStorage that serializes 
    instances to a JSON file and deserializes JSON file to instances.
"""
import json
import os.path

class FileStorage:
    """FileStorage class serializes instances to a JSON file and 
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """Initialize the FileStorage class"""
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.place import Place
        # from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                #    "State": State,
                #    "City": City,
                #    "Amenity": Amenity,
                #    "Place": Place,
                #    "Review": Review
                }
        return classes
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fd:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, fd)

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesnt exist, no exception should be raised"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fd:
                obj_dict = json.load(fd)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict
