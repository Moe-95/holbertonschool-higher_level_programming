#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_str = "argument" if num_args == 1 else "arguments"

    print("{} {}{}.".format(num_args, arg_str, ":" if num_args > 0 else "."))

    for i, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(i, arg))
