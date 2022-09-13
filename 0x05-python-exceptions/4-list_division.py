#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_lists = []
    for n in range(list_length):
        try:
            div = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            div_lists.append(div)

    return (div_lists)
