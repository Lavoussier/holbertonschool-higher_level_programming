#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for x in range(0, list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            new.append(result)
    return new
