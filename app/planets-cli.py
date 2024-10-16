from argparse import ArgumentParser
from methods import *

def AddPlanetCLI(*args):
    planet_values = list(args)[:-1]
    planetary_system = list(args)[-1]
    AddPlanet(planet_values, planetary_system)

global_parser = ArgumentParser(prog="planets-cli")

subparsers = global_parser.add_subparsers(
    title="Available options", help="Available methods to interact with database"
)

get_parser = subparsers.add_parser("get", help="get planet from database")
get_parser.add_argument(dest="provided_args", nargs=1)
get_parser.set_defaults(func=GetPlanet)

add_parser = subparsers.add_parser("add", help='add planet to database. Values must be added separated by a space additionally with the planetary system id at the end')
add_parser.add_argument(dest="provided_args", nargs=13, metavar="entry_value")
add_parser.set_defaults(func=AddPlanetCLI)
# Example: python3 app/planets-cli.py add TestPlanet 4.007 17.200 0.720 0.240 7.250 0.093 0.410 82.000 97.770 "yes" "CO2, N2" 1

update_parser = subparsers.add_parser("update", help="update planet\'s value in database")
update_parser.add_argument(dest="provided_args", nargs=3)
update_parser.set_defaults(func=UpdatePlanet)

delete_parser = subparsers.add_parser("delete", help="delete planet from database")
delete_parser.add_argument(dest="provided_args", nargs=1)
delete_parser.set_defaults(func=DeletePlanet)

args = global_parser.parse_args()
result = args.func(*args.provided_args)