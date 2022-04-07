#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
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
    a = session.query(State).order_by(State.id).all()
    for instance in a:
        print("{}: {}".format(instance.id, instance.name))
        for obj in instance.cities:
            print("\t{}: {}".format(obj.id, obj.name))
    session.close()
