#!/usr/bin/python3
from add_0 import add


def main() -> None:
    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))


if _name_ == "_main_":
    main()
