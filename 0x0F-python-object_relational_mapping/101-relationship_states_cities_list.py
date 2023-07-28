#!/usr/bin/python3
"""script that lists all State objects ina  given db
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localho\
st/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    se = Session()
    q = se.query(State).order_by(State.id)
    for i in q:
        print("{:d}: {:s}".format(i.id, i.name))
        for j in i.cities:
            print("    {:d}: {:s}".format(j.id, j.name))
