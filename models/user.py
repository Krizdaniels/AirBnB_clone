#!/usr/bin/python3
""" This function is for User Class """
from base_model import BaseModel


class User(BaseModel):
    """ User class for inheriting BaseModel """
    def __inint__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
