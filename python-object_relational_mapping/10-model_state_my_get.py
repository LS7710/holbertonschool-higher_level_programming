#!/usr/bin/python3
"""
This script prints the id of the State object with the name passed as an
argument from the database 'hbtn_0e_6_usa'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usr, pwd, db, name = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{usr}:{pwd}@localhost/{db}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
