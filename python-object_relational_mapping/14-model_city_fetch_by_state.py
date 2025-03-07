#!/usr/bin/python3
"""Script that lists all city objets from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

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

    cities = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id).all()
    )
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
