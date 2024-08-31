#!/bin/env python3

import sys
sys.setrecursionlimit(10000000)

def main():
    import pathlib
    with open(pathlib.Path(__file__).parent / "pythonl") as pythonl:
        pythonl_bron_code = pythonl.read()
    exec(pythonl_bron_code, globals() | {'__name__': '__main__'} )

if __name__ == '__main__':
    main()
