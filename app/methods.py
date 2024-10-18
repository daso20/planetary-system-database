from sqlalchemy import select, exc
from sqlalchemy.orm import Session
from connection import engine
from models import PlanetarySystem, Planets
from utils import FormatCSVData, is_number

## Planetary system specific methods
def AddPlanetarySystem(planetary_system_id, planetary_system_name):
    with Session(engine) as session:
        solar_system = PlanetarySystem(
            id = planetary_system_id,
            name = planetary_system_name
        )
        stmt = select(PlanetarySystem).where(PlanetarySystem.name == planetary_system_name)
        ps = session.scalars(stmt).first()
        if ps == None:
            session.add(solar_system)
            session.commit()
        else:
            print(f"Planetary system '{planetary_system_name}' already exists")

## Planet specific methods
def GetPlanet(planet_name, only_test=True):
    with Session(engine) as session:
        stmt = select(Planets).where(Planets.name.in_([planet_name]))
        planet = session.scalars(stmt).first()
        if planet == None and only_test:
            print(f"Planet '{planet_name}' could not be found in database")
            return None
        elif planet == None:
            return None
        
        return planet

## "planet_parameters" needs to be entered as the following:
## ['Earth', '1', '1', '1', '1', '7.25', '0.017', '1', '1', '23.44', 'no', 'N2, O2, Ar']
def AddPlanet(planet_parameters, planetary_system_id):
    result = is_number(planet_parameters[0])
    if result == True:
        print(f"Planet name must a string ('{planet_parameters[0]}' provided)")
        return None
    
    planet_test = GetPlanet(planet_parameters[0], only_test=False)
    if planet_test != None:
        print(f"Planet '{planet_parameters[0]}' already exists")
        return None
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
        try:
            session.commit()
        except exc.IntegrityError as e:
            print(f"An integrity error occurred: " + str(e).split("\n")[1])
            print()
        except exc.DataError as e:
            print(f"A data error occurred: " + str(e).split("\n")[0])
            print(str(e).split("\n")[1])
            print(str(e).split("\n")[2])

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
            print(f"'{parameter}' is not a valid attribute of Planets")
        else:
            setattr(planet, parameter, value)
            try:
                session.commit()
            except exc.DataError as e:
                print(f"A data error occurred: " + str(e).split("\n")[0])
                print(str(e).split("\n")[1])
                print(str(e).split("\n")[2])

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