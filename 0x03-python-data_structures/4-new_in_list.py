#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    replacement = my_list[:]

    if idx <= 0 or idx < length:
        replacement[idx] = element

    return (replacement)
