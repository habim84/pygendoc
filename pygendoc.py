"""
Main python file.
"""
import sys
import os
from argparse import ArgumentParser

MINOR_VERSION = 1
MAJOR_VERSION = 0
PROGRAM_VERSION = str(MAJOR_VERSION)+"."+str(MINOR_VERSION)

if __name__ == "__main__":
    """
    TODO Parse:
    pygendoc [-s stylesheetfile][-f[c][m] filter pydocs by class or method] directory
    """
    parser = ArgumentParser(prog="pygendoc", description="Tool that converts all pydocs into HTML documentation pages.")
    # Version
    parser.add_argument("-v", "--version", action="version", version="%(prog)s "+PROGRAM_VERSION)
    # Stylesheet argument
    parser.add_argument("-s", "--style")
    # Filter argument by class
    parser.add_argument("-fc", "filterclass", action="store_true")
    # Filter argument by methods
    parser.add_argument("-fm", "filtermethod", action="store_true")
    # Directory
    parser.add_argument("directory")
    parser.parse_args()
    