from argparse import ArgumentParser
from methods import *

global_parser = ArgumentParser(prog="planets-cli")

subparsers = global_parser.add_subparsers(
    title="methods", help="Available methods to interact with database"
)

add_parser = subparsers.add_parser("add", help="add planet to database")
add_parser.add_argument(dest="planet_name", nargs=1)
add_parser.set_defaults(func=AddPlanet)

args = global_parser.parse_args()
print(args.func)
print(args.planet_name)