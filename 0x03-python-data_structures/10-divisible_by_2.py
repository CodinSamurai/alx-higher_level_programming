#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_divisibility = []

    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            check_divisibility.append(False)
        else:
            check_divisibility.append(True)

    return (check_divisibility)
