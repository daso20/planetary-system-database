from sqlalchemy import select
from sqlalchemy.orm import Session
from connection import engine
from models import Base, PlanetarySystem, Planets


## Planet specific methods
def GetPlanet(planet_name):
    with Session(engine) as session:
        stmt = select(Planets).where(Planets.name.in_([planet_name]))
        planet = session.scalars(stmt).first()
        return planet

def AddPlanet(planet_name):
    pass

## Add planets from CSV

def UpdatePlanet(planet_name):
    pass

def DeletePlanet(planet_name):
    pass