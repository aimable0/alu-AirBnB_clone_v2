#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', back_populates='state', cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initialize a state object"""
        super().__init__(*args, **kwargs)
        self.storage = storage.all(City)

        # trial
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances with state_id equals to the current State.id"""
            ctys = []
            for value in storage.all(City).values():
                if value.id == self.id:
                    ctys.append(value)
            return ctys
