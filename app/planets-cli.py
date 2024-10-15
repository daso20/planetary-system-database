from argparse import ArgumentParser
from methods import *

def GetPlanetCLI(planet):
    retrieved_planet = GetPlanet(planet)
    pass

def AddPlanetCLI():
    pass

def UpdatePlanetCLI():
    pass

def DeletePlanetCLI():
    pass

global_parser = ArgumentParser(prog="planets-cli")

subparsers = global_parser.add_subparsers(
    title="methods", help="Available methods to interact with database"
)

get_parser = subparsers.add_parser("get", help="get planet from database")
get_parser.add_argument(dest="provided_args", nargs=1)
get_parser.set_defaults(func=GetPlanet)

add_parser = subparsers.add_parser("add", help="add planet to database")
add_parser.add_argument(dest="provided_args", nargs=2)
add_parser.set_defaults(func=AddPlanet)

update_parser = subparsers.add_parser("update", help="update planet\'s value in database")
update_parser.add_argument(dest="provided_args", nargs=3)
update_parser.set_defaults(func=UpdatePlanet)

delete_parser = subparsers.add_parser("delete", help="delete planet from database")
delete_parser.add_argument(dest="provided_args", nargs=1)
delete_parser.set_defaults(func=DeletePlanet)

args = global_parser.parse_args()
#print(args.func)
#print(args.provided_args)
result = args.func(*args.provided_args)
""" 
def process_result(method):
    match method:
        case AddPlanet:
             """