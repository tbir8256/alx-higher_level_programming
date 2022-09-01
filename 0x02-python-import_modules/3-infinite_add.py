#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numarg = 0
    for i in sys.argv[1:]:
        numarg = numarg + int(i)
        print(numarg)
