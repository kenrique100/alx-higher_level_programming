#!/usr/bin/python3
def multiply_by_2(my_dictionary):
    tmp_dictionary = my_dictionary.copy()
    for x in tmp_dictionary.keys():
        tmp_dictionary[x] *= 2
    return (tmp_dictionary)
