#!/usr/bin/python3
""" This function is for Class State """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class for inheriting BaseModel """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = ""
