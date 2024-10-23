from connection import engine
from models import Base
from os import path
from methods import *

## Creates tables if they don't exist
Base.metadata.create_all(engine)

## Adds solar system/planets from example CSV file
basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath, "..", "solarsystemplanets.csv"))

AddPlanetarySystem(1, "Solar System")
AddPlanetsFromCSV(filepath, 1)

def test_Get_And_Add_PS():
    AddPlanetarySystem(2, "Test System")
    result = GetPlanetarySystems()
    assert result[1].attributes_as_list() == [2, 'Test System']

def test_Delete_PS():
    AddPlanetarySystem(3, "Third System")
    result = DeletePlanetarySystem("Third System")
    assert result == None

def test_Get():
    result = GetPlanet('Venus')
    assert result.attributes_as_list() == ['Venus', 1, '0.949', '0.820', '0.720', '0.620', '3.860', '0.007', '-243.020', '0.000', '177.360', 'no', 'CO2, N2']

def test_Update():
    UpdatePlanet('Venus', 'mass', '2.820') # Original = 0.82
    result = GetPlanet('Venus')
    assert str(result.mass) == "2.820"
    UpdatePlanet('Venus', 'mass', '0.82')

def test_Add_and_Delete():
    result = GetPlanet('TestPlanet')
    if result == None:
        AddPlanet(['TestPlanet', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],"1")
        result = GetPlanet('TestPlanet')
        assert result.attributes_as_list() == ['TestPlanet', 1, '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1', '1']
    else:
        print('Planet "TestPlanet" already exists')
    result = DeletePlanet('TestPlanet')
    assert result == None

def test_Get_Planets_PS():
    result = GetPlanet('TestPlanet2')
    if result == None:
        AddPlanet(['TestPlanet2', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],"2")
        result = GetPlanetsFromPS("Test system")
    else:
        print('Planet "TestPlanet2" already exists')
    assert result.attributes_as_list() == ['TestPlanet2', 2, '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1.000', '1', '1']