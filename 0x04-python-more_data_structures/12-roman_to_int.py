#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
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
    roman = 0

    for n in range(len(roman_string)):
        if n > 0 and roman_num[roman_string[n]] > roman_num[roman_string[n - 1]]:
            roman += roman_num[roman_string[n]] - 2 * roman_num[roman_string[n - 1]]
        else:
            roman += roman_num[roman_string[n]]
    return roman
