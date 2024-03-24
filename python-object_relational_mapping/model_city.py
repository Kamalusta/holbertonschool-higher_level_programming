#!/usr/bin/python3
"""doc"""


import sqlalchemy
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """doc"""

    
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True)
