#!/usr/bin/python3
"""
script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Accessing the database"""

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = session.query(State).filter_by(id=2).first()

    if new_state:
        new_state.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")
