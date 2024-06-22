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
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Create an engine that will connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the state with id=2
    state_to_update = session.query(State).filter_by(id=2).one_or_none()

    # Update the state's name if found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
