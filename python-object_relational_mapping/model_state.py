#!/usr/bin/python3
"""python file that contains the class definition of a State and an instance"""
from sqlalchemy import column, integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create instance of declarative_base
Base = declarative_base()

class State(Base):
    """State class that represents the 'states' table"""
    __tablename__ = 'states'
    id = column(integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)
