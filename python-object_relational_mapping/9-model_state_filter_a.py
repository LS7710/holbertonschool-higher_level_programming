#!/usr/bin/python3
"""
t9
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

    # Create a query to select all states containing 'a', order by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print each state that contains the letter 'a'
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
