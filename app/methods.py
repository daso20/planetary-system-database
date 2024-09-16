from sqlalchemy import select
from sqlalchemy.orm import Session
from connection import engine
from models import Base, PlanetarySystem, Planets


## Planet specific methods
def GetPlanet(planet_name):
    with Session(engine) as session:
        stmt = select(Planets).where(Planets.name.in_([planet_name]))
        planet = session.scalars(stmt).first()
        if planet == None:
            print("Planet could not be found in database")
        return planet

## "planet_parameters" needs to be entered as the following:
## ['Earth', '1', '1', '1', '1', '7.25', '0.017', '1', '1', '23.44', 'no', 'N2, O2, Ar']
def AddPlanet(planet_parameters, planetary_system_id):
    with Session(engine) as session:
        dict_of_parameters = {}
        i = 0
        for parameter in planet_parameters:
            dict_of_parameters[parameter] = planet_parameters[i]
            i += 1
        dict_of_parameters['planetary_system_id'] = planetary_system_id
        session_object = Planets(**dict_of_parameters)
        session.add(session_object)
        session.commit()

        return None

## Add planets from CSV

def UpdatePlanet(planet_name, parameter, value):
    with Session(engine) as session:
        stmt = select(Planets).where(Planets.name == planet_name)
        planet = session.scalars(stmt).one()

        if not hasattr(planet, parameter):
            raise AttributeError(f"'{parameter}' is not a valid attribute of Planets")
        else:
            setattr(planet, parameter, value)
            session.commit()
        return planet

def DeletePlanet(planet_name):
    pass