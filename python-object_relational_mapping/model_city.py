#!/usr/bin/python3
"""Defines a State and City class that link to the MySQL tables"""
from sqlalchemy import Column, Integer, String, Foreignkey, create_engine
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

    class City(Base):
        """
        City class that represents the 'cities' table.
        """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)
