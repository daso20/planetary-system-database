import csv

def FormatCSVData(planets_file):
    with open(planets_file) as file:
        lines_read = csv.reader(file)
        planets = list(lines_read)
    
    return planets