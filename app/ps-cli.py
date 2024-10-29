from argparse import ArgumentParser
from methods import GetPlanetarySystems, GetPlanetsFromPS, AddPlanetarySystem, DeletePlanetarySystem

global_parser = ArgumentParser(prog="planets-cli")

subparsers = global_parser.add_subparsers(
    title="Available commands", help="Available planetary system methods to interact with database"
)

get_parser = subparsers.add_parser("getPlanSystems", help="get all planetary systems from database")
get_parser.set_defaults(func=GetPlanetarySystems)

get_planets_parser = subparsers.add_parser("getAllPlanets", help="get all planets from the specified planetary system")
get_planets_parser.add_argument("planetary_system_name")
get_planets_parser.set_defaults(func=GetPlanetsFromPS)

add_parser = subparsers.add_parser("addPlanSystem", help="add planetary system to database")
add_parser.add_argument("planetary_system_id")
add_parser.add_argument("planetary_system")
add_parser.set_defaults(func=AddPlanetarySystem)

delete_parser = subparsers.add_parser("deletePlanSystem", help="delete planetary system from database")
delete_parser.add_argument("planetary_system_name")
delete_parser.set_defaults(func=DeletePlanetarySystem)

args = global_parser.parse_args()

if args.func == GetPlanetarySystems:
    result = args.func()
    for item in result:
        print(item.attributes_as_list())
elif args.func == GetPlanetsFromPS:
    result = args.func(args.planetary_system_name)
    for item in result:
        print(item.attributes_as_list())
else:
    func_args = [getattr(args, arg) for arg in vars(args) if arg != 'func']
    args.func(*func_args)