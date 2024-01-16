#!/usr/bin/python3
""" This function is for Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that is inheriting BaseModel """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    state_id = ""
    name = ""
