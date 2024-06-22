#!/usr/bin/python3
"""
This script prints the first State object from the database 'hbtn_0e_6_usa'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Create an engine that will connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the first state ordered by id (ascending)
    first_state = session.query(State).order_by(State.id).first()

    # Print the result
    if first_state is not None:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
