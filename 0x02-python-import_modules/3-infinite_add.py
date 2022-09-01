#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numarg = 0
    for num in argv[1:]:
        numarg = numarg + int(num)
        print(numarg)
