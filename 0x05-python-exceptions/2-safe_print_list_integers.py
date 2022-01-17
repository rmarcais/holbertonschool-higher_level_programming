#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        a = 0
        for i in range(0, x):
            if isinstance(my_list[i], int) is True:
                print("{:d}".format(my_list[i]), end="")
            else:
                a += 1
        print("")
    except:
        raise
    return i + 1 - a
