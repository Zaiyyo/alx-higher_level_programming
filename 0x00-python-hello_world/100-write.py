#!/usr/bin/python3
import sys
sys.stdout.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")


def print_to_stderr(*a):
    print(*a, file=sys.stderr)


print_to_stderr("1")
