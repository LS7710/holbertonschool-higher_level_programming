#!/usr/bin/python3
"""
This module filters and lists states from a database whose names begin with 'N',
utilizing SQLAlchemy to interact with a MySQL database.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class State(Base):
    """
    Defines the structure of the 'states' table in a MySQL database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

def list_states_with_n_prefix(username, password, dbname):
    """
    Fetches and displays states that start with the letter 'N', ordered by their ID.

    Args:
        username (str): MySQL database username.
        password (str): MySQL database password.
        dbname (str): MySQL database name.
    """
    # Connect to the database using SQLAlchemy engine
    connection_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(connection_url)

    # Setup a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform a query to retrieve all states and sort them by ID
    query_result = session.query(State).order_by(State.id).all()

    # Display states starting with 'N'
    for state in query_result:
        if state.name.startswith('N'):
            print(f"({state.id}, '{state.name}')")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        list_states_with_n_prefix(username, password, dbname)
