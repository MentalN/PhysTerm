#   File: Checkers.py
#   Author: Nawaf Abdullah
#   Creation Date: 7/April/2018
#   Description: Calculating circuit equivalents for resistors, capacitors, and inductors
from Utilities.Checkers import numeric, pause
from Utilities.Logger import logger


def eqv_selector(key):
    if key == 1:
        parallelResistors()
    elif key == 2:
        seriesResistors()
    elif key == 3:
        parallelCapacitors()
    elif key == 4:
        seriesCapacitors()
    elif key == 5:
        parallelInductors()
    elif key == 6:
        seriesInductors()


#   Resistors
def parallelResistors():
    num_R = input("Number of parallel resistors> ")
    try:
        num_R = int(num_R)
    except ValueError:
        print("Please enter an integer value.")
        parallelResistors()

    R_eq = 0
    for x in range(num_R):
        print("Enter the resistance value of Resistor [", x + 1, "]")
        R_n = input("> ")
        try:
            R_n = float(R_n)
        except ValueError:
            R_n = numeric(R_n)
        R_eq += 1 / R_n
    R_eq = R_eq**-1

    print("Equivalent resistance R = ", R_eq)

    log_str = "Equivalent resistance R = " + str(R_eq)
    logger(log_str)

    pause()
    return R_eq


def seriesResistors():
    num_R = input("Number of series resistors> ")
    try:
        num_R = int(num_R)
    except ValueError:
        print("Please enter an integer value.")
        seriesResistors()

    R_eq = 0
    for x in range(num_R):
        print("Enter the resistance value of Resistor [", x + 1, "]")
        R_n = input("> ")
        try:
            R_n = float(R_n)
        except ValueError:
            R_n = numeric(R_n)
        R_eq += R_n

    print("Equivalent resistance R = ", R_eq)

    log_str = "Equivalent resistance R = " + str(R_eq)
    logger(log_str)

    pause()
    return R_eq


#   Capacitors
def parallelCapacitors():
    num_C = input("Number of series capacitors> ")
    try:
        num_C = int(num_C)
    except ValueError:
        print("Please enter an integer value.")
        parallelCapacitors()

    C_eq = 0
    for x in range(num_C):
        print("Enter the capacitance value of capacitor [", x + 1, "]")
        C_n = input("> ")
        try:
            C_n = float(C_n)
        except ValueError:
            C_n = numeric(C_n)
        C_eq += C_n

    print("Equivalent capacitance C = ", C_eq)

    log_str = "Equivalent capacitance C = " + str(C_eq)
    logger(log_str)

    pause()
    return C_eq


def seriesCapacitors():
    num_C = input("Number of series capacitors> ")
    try:
        num_C = int(num_C)
    except ValueError:
        print("Please enter an integer value.")
        parallelCapacitors()

    C_eq = 0
    for x in range(num_C):
        print("Enter the capacitance value of capacitor [", x + 1, "]")
        C_n = input("> ")
        try:
            C_n = float(C_n)
        except ValueError:
            C_n = numeric(C_n)
        C_eq += 1 / C_n
    C_eq = C_eq**-1

    print("Equivalent capacitance C = ", C_eq)

    log_str = "Equivalent capacitance C = " + str(C_eq)
    logger(log_str)

    pause()
    return C_eq


#   Inductors
def parallelInductors():
    num_L = input("Number of parallel inductors> ")
    try:
        num_L = int(num_L)
    except ValueError:
        print("Please enter an integer value.")
        parallelInductors()

    L_eq = 0
    for x in range(num_L):
        print("Enter the inductance value of inductors [", x + 1, "]")
        L_n = input("> ")
        try:
            L_n = float(L_n)
        except ValueError:
            L_n = numeric(L_n)
        L_eq += 1 / L_n
    L_eq = L_eq**-1

    print("Equivalent inductance L = ", L_eq)

    log_str = "Equivalent inductance L = " + str(L_eq)
    logger(log_str)

    pause()
    return L_eq


def seriesInductors():
    num_L = input("Number of series inductors> ")
    try:
        num_L = int(num_L)
    except ValueError:
        print("Please enter an integer value.")
        seriesInductors()

    L_eq = 0
    for x in range(num_L):
        print("Enter the capacitance value of inductors [", x + 1, "]")
        L_n = input("> ")
        try:
            L_n = float(L_n)
        except ValueError:
            L_n = numeric(L_n)
        L_eq += L_n

    print("Equivalent inductance L = ", L_eq)

    log_str = "Equivalent inductance L = " + str(L_eq)
    logger(log_str)

    pause()
    return L_eq