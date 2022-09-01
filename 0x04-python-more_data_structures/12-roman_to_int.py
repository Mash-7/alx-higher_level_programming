#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not ininstance(roman_string, str) or roman_string is None):
        return (0)

    roman_num = [
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                ]
    i = 0
    last = 0

    for n in range(len(roman_string)):
        for dig in roman_num:
           if n == dig[0]:
           if last == 0 or last >= dig[1]:
                n += dig[1]
           elif last < dig[1]:
                num += dig[1] - (last * 2)
                
           last = dig[1]
    return n
