#!/usr/bin/python3
def weight_average(my_list=[]):
    coeff = 0
    total = 0
    if my_list is None or my_list == 0:
        return 0
    for i in range(len(my_list)):
        total += my_list[i][0] * my_list[i][1]
        coeff = coeff + my_list[i][1]
    return total / coeff
