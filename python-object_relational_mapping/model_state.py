#!/usr/bin/python3
"""python file that contains the class definition of a State and an instance"""
from sqlalchemy import column, integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys
Base = declarative_base()


class State(Base):
    """State class that represents the 'states' table"""
    __tablename__ = 'states'
    id = column(integer, primary_key=True, autoincrement=True, nullable=False)
    name = column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
