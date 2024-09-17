from os import path
from sqlalchemy.orm import Session
from connection import engine
from models import Base, PlanetarySystem, Planets
from utils import FormatCSVData
from methods import AddPlanetarySystem

## Creates tables if they don't exist
Base.metadata.create_all(engine)

## Adds solar system/planets from CSV file
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "solarsystemplanets.csv"))

with Session(engine) as session:
    solar_system = PlanetarySystem(
        id = 1,
        name = "Solar System"
    )
    session.add(solar_system)

    list_of_planets = FormatCSVData(filepath)

    parameters_of_planet = list_of_planets[0]

    for planet in list_of_planets[1:]:
        dict_of_parameters = {}
        i = 0
        for parameter in parameters_of_planet:
            dict_of_parameters[parameter] = planet[i]
            i += 1
        dict_of_parameters['planetary_system_id'] = 1
        session_object = Planets(**dict_of_parameters)
        session.add(session_object)

    session.commit()