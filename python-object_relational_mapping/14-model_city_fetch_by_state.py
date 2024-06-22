#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    usr, pwd, db = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{usr}:{pwd}@localhost/{db}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Join the states and cities tables to fetch the data sorted by city IDs
    results = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
