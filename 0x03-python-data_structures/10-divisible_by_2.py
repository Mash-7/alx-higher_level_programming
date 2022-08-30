#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    find_mul = []

    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            find_mul.append(True)
        else:
            find_mul.append(False)
    return (find_mul)
