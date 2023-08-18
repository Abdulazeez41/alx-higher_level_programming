#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = list(set(my_list))
    sum = 0
    for i in range(len(y)):
        sum += y[i]
    return sum
