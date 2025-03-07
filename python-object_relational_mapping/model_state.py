#!/usr/bin/python3
"""
Defines a State class that links to the MySQL table 'states'.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
