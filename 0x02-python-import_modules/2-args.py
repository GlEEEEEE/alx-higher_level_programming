#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args == 0:
        print("Number of argument(s): 0.")
    else:
        plural = "s" if num_args > 1 else ""
        print("Number of argument{}: {}{}".format(
            plural, num_args, "s" if plural else ""), end="\n" if num_args == 0 else ":")

        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
