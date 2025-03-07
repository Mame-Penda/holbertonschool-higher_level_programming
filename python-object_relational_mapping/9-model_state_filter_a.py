#!/usr/bin/python3
""" script that lists all State objects that contain the letter"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)  # Ajout explicite de bind=
    session = Session()

    # Liste tous les objets State en les triant par id
    states = session.query(State).filter(State.name.like('%a%')
                                         ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
