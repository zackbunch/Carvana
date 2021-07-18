from sqlalchemy import Column, ForeignKey, Integer, String, create_engine

engine = create_engine('sqlite:///carvana.db', echo = False)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
import sqlite3

import pandas as pd
from sqlalchemy.orm import relationship


class Location(Base):
    __tablename__ = 'locations'
    code = Column(String, primary_key = True)
    latitude = Column(String)
    longitude = Column(String)
    owned = Column(String)

class Trip(Base):
    __tablename__ = 'trips'
    route = Column(String, primary_key=True)
    origin = Column(String, ForeignKey('locations.code'))
    origin_id = relationship("Location", foreign_keys=[origin])

    destination= Column(String, ForeignKey('locations.code'))
    destination_id = relationship("Location", foreign_keys=[destination])
    capacity = Column(Integer)

Base.metadata.create_all(engine)


def populateDB():
    conn = sqlite3.connect('carvana.db')
    locationsDF = pd.read_csv('data/locations.csv')
    tripsDF = pd.read_csv('data/trips.csv')
    # write the data to a sqlite table
    locationsDF.to_sql('locations', conn, if_exists='replace', index = False)
    tripsDF.to_sql('trips', conn, if_exists='replace', index = False)






if __name__ == "__main__":
    populateDB()
