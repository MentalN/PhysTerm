#   File: Checkers.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: several functions that checks for input


def numeric(num):
    if isinstance(num, int) is False and isinstance(num, float) is False:
        num = input("Error, please enter a numeric value > ")
        try:
            float(num)
        except ValueError:
            numeric(num)
    else:
        pass
    return num


