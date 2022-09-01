#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not ininstance(roman_string, str) or roman_string is None):
        return (0)

    roman_num = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
    Keys = list(roman_num.keys())
    i = 0

    for n in range(len(roman_string)):
        if roman_num.get(roman_string[n], 0) == 0:
            return (0)
        if (n != (len(roman_string) - 1) and
                roman_num[roman_string[n]] < roman_num[roman_string[n + 1]]):
            i += roman_num[roman_string[n]] * -1

        else:
            i += roman_num[roman_string[n]]
            return (i)
