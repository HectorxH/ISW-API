from requests import get
import argparse

URL = "http://18.221.241.253:8000/"

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

verbose = parser.parse_args().verbose


def vprint(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)


vprint("Probando: [GET] /habilitaciones/capacitaciones")
test1 = get(URL+"/habilitaciones/capacitaciones")

print(test1)
