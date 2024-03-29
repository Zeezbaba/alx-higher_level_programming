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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    california = State(name='California')
    san_francisco = City(name='San Francisco')
    california.cities.append(san_francisco)

    session.add(california)
    session.commit()
    session.close()
