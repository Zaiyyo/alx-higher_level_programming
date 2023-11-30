#!/usr/bin/python3
from sys import argv

def main():
    sum = 0
    for ii in range(1, len(argv)):
        sum = sum + int(argv[1])
    print(sum)

if __name__ == "__main__":
    main()




