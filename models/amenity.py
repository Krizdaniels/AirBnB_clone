#!/usr/bin/python3
""" This function is for Class Amenity """
from base_model import BaseModel
 

class Amenity(BaseModel):
    """ Amenity class for inheriting BaseModel """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
