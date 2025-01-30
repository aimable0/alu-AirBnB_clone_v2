#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel

# from models.base_model import Base
# from sqlalchemy import String, Column, ForeignKey


class Place(BaseModel):
    """A place to stay"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
