#!/usr/bin/python3
"""
This script changes the name of the State object with id=2
from the database 'hbtn_0e_6_usa' to 'New Mexico'.
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

    state_to_update = session.query(State).filter_by(id=2).one_or_none()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
