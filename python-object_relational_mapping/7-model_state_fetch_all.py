#!/usr/bin/python3
"""
This script lists all State objects from the database 'hbtn_0e_6_usa'
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

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a query to select all states and order them by id ascending
    states = session.query(State).order_by(State.id).all()

    # Print each state from the query
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
