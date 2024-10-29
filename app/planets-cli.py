from argparse import ArgumentParser
from methods import GetPlanet, AddPlanet, AddPlanetsFromCSV, UpdatePlanet, DeletePlanet

def AddPlanetCLI(*args):
    planet_values = list(args)[:-1]
    planetary_system = list(args)[-1]
    AddPlanet(planet_values, planetary_system)

global_parser = ArgumentParser(prog="planets-cli")

subparsers = global_parser.add_subparsers(
    title="Available commands", help="Available planet methods to interact with database"
)

get_parser = subparsers.add_parser("get", help="get planet from database")
get_parser.add_argument('planet_name')
get_parser.set_defaults(func=GetPlanet)

add_parser = subparsers.add_parser("add", help='add planet to database. "name" and "planetary_system_id" are required, the rest can be entered specifying the respective flag')
add_parser.add_argument('name')
add_parser.add_argument('--equatorial_diameter')
add_parser.add_argument('--mass')
add_parser.add_argument('--semi_major_axis')
add_parser.add_argument('--orbital_period')
add_parser.add_argument('--inclination_to_suns_equator')
add_parser.add_argument('--orbital_eccentricity')
add_parser.add_argument('--rotation_period')
add_parser.add_argument('--confirmed_moons')
add_parser.add_argument('--axial_tilt')
add_parser.add_argument('--rings')
add_parser.add_argument('--atmosphere')
add_parser.add_argument('planetary_system_id')
add_parser.set_defaults(func=AddPlanetCLI)
# Example: python3 app/planets-cli.py add TestPlanet 1 --equatorial_diameter=4.007 --mass=17.200 --semi_major_axis=0.720 --orbital_period=0.240 --inclination_to_suns_equator=7.250
# --orbital_eccentricity=0.093 --rotation_period=0.410 --confirmed_moons=82.000 --axial_tilt=97.770 --rings="yes" --atmosphere="CO2, N2"

addCSV_parser = subparsers.add_parser("addCSV", help='add planets from CSV file')
addCSV_parser.add_argument('csv_file')
addCSV_parser.add_argument('planetary_system_id')
addCSV_parser.set_defaults(func=AddPlanetsFromCSV)
                        
update_parser = subparsers.add_parser("update", help="update planet\'s value in database")
update_parser.add_argument('planet_name')
update_parser.add_argument('parameter')
update_parser.add_argument('value')
update_parser.set_defaults(func=UpdatePlanet)

delete_parser = subparsers.add_parser("delete", help="delete planet from database")
delete_parser.add_argument('planet_name')
delete_parser.set_defaults(func=DeletePlanet)

args = global_parser.parse_args()

if args.func in [AddPlanetCLI, UpdatePlanet, AddPlanetsFromCSV]:
    func_args = [getattr(args, arg) for arg in vars(args) if arg != 'func']
    args.func(*func_args)
elif args.func == GetPlanet:
    result = args.func(args.planet_name)
    if result != None: print(result.attributes_as_list())
else:
    result = args.func(args.planet_name)