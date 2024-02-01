#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("")
    except IndexError:
        print("")
        return i if i < len(my_list) else i + 1
    return x
