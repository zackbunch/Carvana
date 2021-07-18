from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import join
from models import Location, Trip, engine
Session = sessionmaker(bind = engine)
session = Session()



def getLocationCode(desiredLocation):
    for l in session.query(Location) \
    .filter(Location.code==desiredLocation) \
    .all():
        isOwned = ""
        if l.owned == 1:
            isOwned = "Owned by Carvana"
        else:
            isOwned = "Not owned by Carvana"
        print("{}: Lat: {}, Long: {}, {}".format(desiredLocation, l.latitude, l.longitude, isOwned))
        
def getOrigin(desiredLocation):
    for l, t in session.query(Location, Trip) \
    .join(Trip, Trip.origin == Location.code) \
    .filter(Location.code==desiredLocation) \
    .all():
        isOwned = ""
        if l.owned == 1:
            isOwned = "Owned by Carvana"
        else:
            isOwned = "Not owned by Carvana"
        print("Origin Trips: {} to {} ({} weekly capacity)".format(t.origin, t.destination, t.capacity))

def getDestination(desiredLocation):
    for l, t in session.query(Location, Trip) \
    .join(Trip, Trip.destination == Location.code) \
    .filter(Location.code==desiredLocation) \
    .all():
        isOwned = ""
        if l.owned == 1:
            isOwned = "Owned by Carvana"
        else:
            isOwned = "Not owned by Carvana"
        print("Destination Trips: {} to {} ({} weekly capacity)".format(t.origin, t.destination, t.capacity))
    

def aggregateTrip(desiredLocation):
    getLocationCode(desiredLocation)
    getOrigin(desiredLocation)
    getDestination(desiredLocation)




if __name__ == "__main__":
    #joinTables()
    # getLocationCode("KSC")
    # getOrigin("KSC")
    # getDestination("KSC")
    aggregateTrip("WIND")
 

   
