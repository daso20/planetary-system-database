from methods import GetPlanet

def test_Get():
    result = GetPlanet('Venus')
    assert result.attributes_as_list() == ['Venus', 1, '0.949', '0.82', '0.72', '0.62', '3.86', '0.007', '-243.02', '0', '177.36', 'no', 'CO2, N2']