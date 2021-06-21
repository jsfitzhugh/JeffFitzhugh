#!\Users\f791345\Documents\Scripts\PytonScripts

import argparse

def main():
    """Main entrypoint of the cli."""
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='command')

    # first command
    add = subparsers.add_parser(commands.ADD)
    add.add_argument("numbers", nargs="+", type=int)

    #second command
    sub = subparsers.add_parser(commands.SUBTRACT) 
    sub.add_argument('numbers', nargs='+', type=int)


    parser.add_argument('test')

    args = parser.parse_args()

    print(args)