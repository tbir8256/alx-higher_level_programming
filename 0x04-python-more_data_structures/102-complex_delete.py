#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_list = list(a_dictionary.keys())
    for key in a_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
            return a_dictionary 
