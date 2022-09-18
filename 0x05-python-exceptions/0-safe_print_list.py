#!/usr/bin/python3
def safe_pritn_list(my_list=[], x=0):
    a = 0
    for i in ranbe(x):
        try:
            print(my_list=[i], end="")
            a += 1
        except IndexError:
            break
        print()
        return a
