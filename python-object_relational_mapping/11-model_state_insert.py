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

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    session.close()
