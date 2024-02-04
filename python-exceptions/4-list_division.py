#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            division = 0
            if i < len(my_list_1) and i < len(my_list_2) and my_list_2[i] != 0:
                division = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
            elif my_list_2[i] == 0:
                print("division by 0")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(division)
    return result
