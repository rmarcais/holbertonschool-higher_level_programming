#!/usr/bin/python3
"""
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

import sqlalchemy as sa
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    s = Session()
    a = s.query(State).filter(State.name ==
                              sys.argv[4]).order_by(State.id).all()
    if a != []:
        for instance in a:
            print("{}".format(instance.id))
    else:
        print("Not found")
    s.close()
