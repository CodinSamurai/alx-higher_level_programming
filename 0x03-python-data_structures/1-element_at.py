#!/usr/bin/python3
def element_at(my_data, index):
    if index < 0:
        return (None)

    length = len(my_data)

    if index > length - 1:
        return (None)

    return(my_data[index])
