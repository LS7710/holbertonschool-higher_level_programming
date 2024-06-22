#!/usr/bin/python3

"""
Defines the State class with SQLAlchemy
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Base instance for declarative system
Base = declarative_base()


class State(Base):
    """State class:
    - inherits from Base
    - links to the MySQL table states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
