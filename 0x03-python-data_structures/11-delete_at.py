#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    final = []
    for i in range(len(my_list)):
        if i == idx:
            if i <= 0 and i < len(my_list):
                return (my_list)
            my_list.remove(i)
            final.append(i)
    return(final)
