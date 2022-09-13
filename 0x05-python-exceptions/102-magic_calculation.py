#!/usr/bin/python3
def magic_calculation(a, b):
    owari = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception("Too far")
            else:
                owari += (a ** b) / n

        except:
            owari = b + a
            break
    return (owari)
