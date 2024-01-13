#!/usr/bin/python3
"""

"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return FileStorage.__file_path

    @property
    def objects(self):
        return FileStorage.__objects

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                cls_name, obj_id = key.split('.')
                cls = classes[cls_name]
                FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

