from argparse import ArgumentParser
from methods import *

parser = ArgumentParser(prog="planets-cli",
                        description="Interface to postgres database"
)

parser.add_argument("--add")
parser.add_argument("--addPlanetsFromCSV")
parser.add_argument("--get")
parser.add_argument("--update")
parser.add_argument("--delete")
args = parser.parse_args()
print(args)