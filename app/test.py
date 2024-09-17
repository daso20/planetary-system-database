from methods import GetPlanet, AddPlanet, UpdatePlanet, DeletePlanet

def test_Get():
    result = GetPlanet('Venus')
    assert result.attributes_as_list() == ['Venus', 1, '0.949', '0.82', '0.72', '0.62', '3.86', '0.007', '-243.02', '0', '177.36', 'no', 'CO2, N2']

def test_Update():
    UpdatePlanet('Venus', 'mass', '2.82') # Original = 0.82
    result = GetPlanet('Venus')
    assert result.mass == "2.82"
    UpdatePlanet('Venus', 'mass', '0.82')

def test_Add_and_Delete():
    result = GetPlanet('TestPlanet')
    if result == None:
        AddPlanet(['TestPlanet', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],"1")
        result = GetPlanet('TestPlanet')
        assert result.attributes_as_list() == ['TestPlanet', 1, '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    else:
        print('Planet "TestPlanet" already exists')
    result = DeletePlanet('TestPlanet')
    assert result == None