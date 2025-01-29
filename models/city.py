#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, ForeignKey, Column
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False) # still some fix to be done
    # some instruction about the relationship (city - state)... to be revised

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id

