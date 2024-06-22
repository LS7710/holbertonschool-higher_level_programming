#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database 'hbtn_0e_6_usa'
and prints the new state's id.
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
