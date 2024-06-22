#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database 'hbtn_0e_6_usa'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usr, pwd, db = sys.argv[1:]

    engine = create_engine(
        f'mysql+mysqldb://{usr}:{pwd}@localhost/{db}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()

