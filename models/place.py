#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """A place to stay"""

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship(
            "Review", back_populates="place", cascade="all, delete-orphan"
        )
    else:
        # in case of file_storage
        name = ""
        city_id = ""  # it will be the City.id
        user_id = ""  # it will be the User.id
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []  # it will be the list of Amenity.id later

    def __init__(self, *args, **kwargs):
        """initialize an instance of place"""
        super().__init__(*args, **kwargs)

    
    @property
    def reviews(self):
        from models.review import Review
        from models import storage

        # list generation
        all_reviews = []
        for obj in storage.all(Review).values():
            if obj.place_id == self.id:
                all_reviews.append(obj)
        return all_reviews
