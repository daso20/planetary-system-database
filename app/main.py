from os import path
from connection import engine
from models import Base
from methods import AddPlanetarySystem, AddPlanetsFromCSV

## Creates tables if they don't exist
Base.metadata.create_all(engine)

## Adds solar system/planets from CSV file
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "solarsystemplanets.csv"))

AddPlanetarySystem(1, "Solar System")
AddPlanetsFromCSV(filepath, 1)
#AddPlanetsFromCSV("filepath", 1)