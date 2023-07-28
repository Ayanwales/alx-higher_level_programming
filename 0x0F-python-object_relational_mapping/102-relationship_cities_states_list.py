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
    q = se.query(City).order_by(City.id)
    for i in q:
        print("{:d}: {:s} -> {:s}".format(i.id, i.name, i.state.name))
