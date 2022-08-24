#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastD = number % 10
    else:
        lastD = number % -10
        lastD *= -1

    print(f"{lastD:d}", end="")
    return (lastD)
