#!/usr/bin/python3
def simple_delete(dict_input, key=""):
    if key in dict_input:
        del dict_input[key]
    return dict_input
