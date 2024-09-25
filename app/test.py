from methods import GetPlanet, AddPlanet, UpdatePlanet, DeletePlanet

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