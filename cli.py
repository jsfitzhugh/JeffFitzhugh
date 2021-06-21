    #!\Users\f791345\Documents\Scripts\PytonScripts

ADD = 'add'
SUBTRACT = 'subtract'

import commands
import argparse

def multiply(ns):
    """Multiplies all of the numbers contained in ns."""
    result = 1
    for n in ns:
        result *= n
    return result


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(commands.ADD)
    add.add_argument(
        "numbers",
        nargs="+",
        type=int,
    )

    sub = subparsers.add_parser(commands.SUBTRACT)
    sub.add_argument(
        "numbers",
        nargs="+",
        type=int,
    )

    mul = subparsers.add_parser(commands.MULTIPLY)
    mul.add_argument("numbers", nargs="+", type=int)

    div = subparsers.add_parser(commands.DIVIDE)
    div.add_argument("numbers", nargs="+", type=int)


    args = parser.parse_args()

    if args.command == commands.ADD:
        result = sum(args.numbers)
        operation = " + ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    elif args.command == commands.SUBTRACT:
        first, *rest = args.numbers
        result = first - sum(rest)
        operation = " - ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    elif args.command == commands.MULTIPLY:
        result = multiply(args.numbers)
        operation = " x ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    elif args.command == commands.DIVIDE:
        first, *rest = args.numbers
        result = first / multiply(rest)
        operation = " ÷ ".join(str(i) for i in args.numbers)
        print(f"The result of {operation} is {result}.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

    #complete commands.py

    ADD = "add"
SUBTRACT = "sub"
MULTIPLY = "mul"
DIVIDE = "div"
