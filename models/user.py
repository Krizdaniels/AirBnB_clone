#!/usr/bin/python3
""" This function is for User Class """
from models.base_model import BaseModel

class User(BaseModel):
    """ User class for inheriting BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
