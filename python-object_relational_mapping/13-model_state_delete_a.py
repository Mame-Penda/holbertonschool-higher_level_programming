#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)  # Ajout explicite de bind=
    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
        session.commit()

        session.close()
