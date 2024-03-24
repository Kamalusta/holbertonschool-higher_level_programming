#!/usr/bin/python3
"""doc"""


from model_state import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'))
