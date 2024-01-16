#!/usr/bin/python3
""" This funtion is for Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class for inheriting BaseModel """

    def __init__(self, *args, **kwargs):
        super().__init__(*argds, **kwargs)

    place_id = ""
    user_id = ""
    text = ""
