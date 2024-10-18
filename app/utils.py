import csv

def FormatCSVData(planets_file):
    file_header = ['name', 'equatorial_diameter', 'mass', 'semi_major_axis', 'orbital_period', 'inclination_to_suns_equator', 'orbital_eccentricity', 'rotation_period', 'confirmed_moons', 'axial_tilt', 'rings', 'atmosphere']
    try:
        with open(planets_file) as file:
            lines_read = csv.reader(file)
            planets = list(lines_read)
            if planets[0] != file_header:
                print("Incorrect file header row")
                return None
            for i in range(len(planets)):
                if len(planets[i]) != 12:
                    print(f"Amount of parameters given in line {i + 1} is not enough/more than the expected")
                    return None
            return planets
    except FileNotFoundError:
        print(f"The file could not be found")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False