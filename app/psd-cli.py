from argparse import ArgumentParser

parser = ArgumentParser(prog="psd-cli",
                        description="Interface to postgres database"
)

parser.add_argument("planetary-system")
parser.add_argument("planet")
args = parser.parse_args()
