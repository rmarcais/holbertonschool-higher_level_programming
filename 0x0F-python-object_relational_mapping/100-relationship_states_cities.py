#!/usr/bin/python3
"""
script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""

import sqlalchemy as sa
import sys
from sqlalchemy import Sequence
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()
    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Fransisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()
