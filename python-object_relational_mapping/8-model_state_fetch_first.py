#!/usr/bin/python3
"""
lists all state objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    first = session.query(State).order_by(State.id).first()
    try:
        print("{}: {}".format(first.id, first.name))
    except SQLAlchemyError as e:
        print("Nothing")
    session.close()
