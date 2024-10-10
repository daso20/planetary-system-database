from argparse import ArgumentParser

parser = ArgumentParser(prog="ps-cli",
                        description="Interface to postgres database"
)

#parser.add_argument("planetary-system")
args = parser.parse_args()