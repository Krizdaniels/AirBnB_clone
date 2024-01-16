#!/usr/bin/python3
""" The class FileStorage serializes instances to a JSON file
    and deserializes JSON file to instances """

import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ The Construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ To return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ It sets in dictionary the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ It serializes objects to the JSON file (path: __file_path) """
        save_dict = {key: obj.to_dict() for key, obj in
                     FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(save_dict, file)

    def reload(self):
        """ Load objects from JSON file to __objects. """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                load_dict = json.load(file)
                for key, obj_dict in load_dict.items():
                    class_name = obj_dict['__class__']
                    del obj_dict['__class__']
                    obj = globals()[class_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
