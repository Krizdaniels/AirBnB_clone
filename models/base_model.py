#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
import uuid
import models


class BaseModel:
    """ class definitions construct """

    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

            else:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()

        def __str__(self):
            """ String representation of BaseModel instance"""
            return "[{}] ({}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

        def save(self):
            """ Save function """
        self.updated_at = datetime.now()
        models.storage.save()

        def to_dict(self):
            """ Return object attributes to  dictionary """
            obj_dict = Self.__dict__.copy()
            obj_dict['__class__'] = self.class__.__name__
            obj_dict['created_at'] = self.created_at.isoformat()
            obj_dict['updated_at'] = self.updated_at.isoformat()
            return obj_dict

# Example usage:
# my_instance = BaseModel(name="exmple")
# my_dict = my_instance.to_dict()
# my_json_string = json.dumps(my_dict)
# my_instance.save() # Implement save method in FIleStorage
