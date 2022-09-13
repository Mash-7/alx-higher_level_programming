#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        owari = fct(*args)
    except Exception as n:
        sys.stderr.write("Exception: {}\n".format(n))
        owari = None

    return (owari)
