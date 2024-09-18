import csv

def FormatCSVData(planets_file):
    try:
        with open(planets_file) as file:
            lines_read = csv.reader(file)
            planets = list(lines_read)
            return planets
    except FileNotFoundError:
        print(f"The file could not be found")