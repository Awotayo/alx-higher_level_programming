#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return (None)
    r_list = []
    for i in range(len(my_list)):
        if my_list[1] % 2 == 0:
            r_list.append(True)
        else:
            r_list.append(False)
    return (r_list)
