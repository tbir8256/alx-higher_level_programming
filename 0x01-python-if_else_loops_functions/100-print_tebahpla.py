#!/usr/bin/python3
# Author -Bamidele Adefolaju

i = 0
for c in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(chr(c - 33)), end="")
