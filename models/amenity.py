#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv


class Amenity(BaseModel):
    """info to be filled"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        ...
    else:
        name = ""
