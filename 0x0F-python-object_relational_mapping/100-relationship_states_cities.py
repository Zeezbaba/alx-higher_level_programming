#!/usr/bin/python3
"""
script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """Accessing the database"""

    db = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)

    session = Session()

    california = State(name="California", cities=[City(name="San Francisco")])
    session.add(california)
    session.commit()
    session.close()
