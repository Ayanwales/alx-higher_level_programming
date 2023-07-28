#!/usr/bin/python3
"""contains the class definition State and an instance Base"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """Class state, has id and name attributes"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state')
