#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(min(list_length, len(my_list_1), len(my_list_2))):
        try:
            res = my_list_1[i] / my_list_2[i]
        except (IndexError, ZeroDivisionError, TypeError) as e:
            res = 0
            print(e.__class__.__name__.lower())
        finally:
            new.append(res)
    return new
