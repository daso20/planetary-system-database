from sqlalchemy import select
from sqlalchemy.orm import Session
from connection import engine
from models import PlanetarySystem, Planets
from utils import FormatCSVData

## Planetary system specific methods
def AddPlanetarySystem(planetary_system_id, planetary_system_name):
    with Session(engine) as session:
        solar_system = PlanetarySystem(
            id = planetary_system_id,
            name = planetary_system_name
        )
        session.add(solar_system)
        session.commit()

## Planet specific methods
def GetPlanet(planet_name):
    with Session(engine) as session:
        stmt = select(Planets).where(Planets.name.in_([planet_name]))
        planet = session.scalars(stmt).first()
        if planet == None:
            print(f"Planet {planet_name} could not be found in database")
            return None
        return planet

## "planet_parameters" needs to be entered as the following:
## ['Earth', '1', '1', '1', '1', '7.25', '0.017', '1', '1', '23.44', 'no', 'N2, O2, Ar']
def AddPlanet(planet_parameters, planetary_system_id):
    with Session(engine) as session:
        dict_of_parameters = {}
        i = 0
        list_of_parameters = ['name', 'equatorial_diameter', 'mass', 'semi_major_axis', 'orbital_period', 'inclination_to_suns_equator', 'orbital_eccentricity', 'rotation_period', 'confirmed_moons', 'axial_tilt', 'rings', 'atmosphere']
        for parameter in planet_parameters:
            dict_of_parameters[list_of_parameters[i]] = parameter
            i += 1
        dict_of_parameters['planetary_system_id'] = planetary_system_id
        session_object = Planets(**dict_of_parameters)
        session.add(session_object)
        session.commit()

        return None

def AddPlanetsFromCSV(csv_file, planetary_system_id):
    list_of_planets = FormatCSVData(csv_file)
    if list_of_planets != None:
        for planet_parameters in list_of_planets[1:]:
            AddPlanet(planet_parameters, planetary_system_id)

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
    with Session(engine) as session:
        stmt = session.query(Planets).filter(Planets.name == planet_name).first()
        if stmt == None:
            print(f"Planet {planet_name} does not exist in database")
            return "Error"
        else:
            session.delete(stmt)
            session.commit()
            return None