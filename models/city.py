#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
# from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship(
        "Place", back_populates="cities", cascade="all, delete-orphan"
    )

    def __init__(self, *args, **kwargs):
        """Initialize a City Instance"""
        super().__init__(*args, **kwargs)
