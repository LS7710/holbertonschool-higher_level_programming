#!/usr/bin/python3
"""Lists all states in the database."""
import sys
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """Defines the State model."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

def list_states(username, password, dbname):
    """Connects to the MySQL database and lists all states."""
    # Create the connection string
    connection_string = f"mysql+mysqldb://{username}:{password}@localhost/{dbname}"

    # Initialize the database engine
    engine = create_engine(connection_string)

    # Configure a Session class
    Session = sessionmaker(bind=engine)

    # Start a new session
    session = Session()

    # Query all states, ordered by id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each state
    for state in states:
        print(f"({state.id}, '{state.name}')")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Call the function to list states
    list_states(username, password, dbname)
