#!/usr/bin/python3
def delete_at(my_data=[], index=0):
    length = len(my_data)

    if index >= length or index < 0:
        return (my_data)

    del my_data[index]

    return (my_data)
