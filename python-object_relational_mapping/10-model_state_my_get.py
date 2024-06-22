#!/usr/bin/python3
"""
This script prints the id of the State object with the name passed as argument
from the database 'hbtn_0e_6_usa'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username, mysql_password, database_name, state_name_to_search = sys.argv[1:]

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

    # Query for the state with the given name (SQL injection free)
    state = session.query(State).filter(State.name == state_name_to_search).first()

    # Print the state id if found, otherwise print 'Not found'
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
