#!/usr/bin/env python3
"""
This script lists all states with names starting with 'N' from the database
hbtn_0e_0_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class mapped to the 'states' table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)

def fetch_states_with_n(user, passwd, db):
    """
    Connect to the MySQL database and fetch all states with names
    starting with 'N', ordered by their IDs.
    
    Args:
        user (str): MySQL username.
        passwd (str): MySQL password.
        db (str): Database name.
    """
    # Create engine and bind it to the session
    engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch and print states starting with 'N'
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if state.name.startswith('N'):
            print(f"({state.id}, '{state.name}')")
    
    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, dbname = sys.argv[1:4]
        fetch_states_with_n(username, password, dbname)
