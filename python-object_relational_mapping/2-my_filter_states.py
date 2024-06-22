#!/usr/bin/python3
# A simple script to find states in a database matching a name

import MySQLdb
import sys
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, sessionmaker

# Set up base class
Base = declarative_base()

class State(Base):
    # Table configuration
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

def find_states(username, password, dbname, state_name):
    # This function looks for states with a given name
    connection_string = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
    engine = create_engine(connection_string)

    # Make session class and instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Prepare and run the query
    sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name)
    result = session.execute(sql_query).fetchall()

    # Display results
    for state in result:
        print(f"({state.id}, '{state.name}')")

    session.close()  # Don't forget to close the session

# Check if script is run as main
if __name__ == "__main__":
    if len(sys.argv) == 5:
        user = sys.argv[1]
        passw = sys.argv[2]
        db = sys.argv[3]
        name_of_state = sys.argv[4]
        find_states(user, passw, db, name_of_state)
