#   File: Checkers.py
#   Author: Nawaf Abdullah
#   Creation Date: 5/April/2018
#   Description: Drag Calculations
from Utilities.Checkers import numeric
from Utilities.Constants import a_g
from math import sqrt

Cd_dict = {'sphere':      0.47, 'half sphere':   0.42, 'cone': 0.50, 'cube': 1.05,
           'angled cube': 0.80, 'long cylinder': 0.82, 'short cylinder':     1.15,
           'airfoil':    0.045, 'half airfoil':  0.09, 'bullet': 0.295, 'prism': 1.14,
           'flat': 1.28}


def terminalVelocity():
    print("Terminal Velocity")

    m = input("Mass of the object> ")
    try:
        m = float(m)
    except ValueError:
        m = numeric(m)

    Cd = input("Drag coefficient>")
    if Cd not in Cd_dict:
        try:
            Cd = float(Cd)
        except ValueError:
            Cd = numeric(Cd)
    elif Cd in Cd_dict:
        Cd = Cd_dict[Cd]

    A = input("Frontal surface area> ")
    try:
        A = float(A)
    except ValueError:
        A = numeric(A)

    p = input("medium density> ")
    try:
        p = float(p)
    except ValueError:
        p = numeric(p)

    v_term = sqrt((2*m*a_g)/(Cd*p*A))
    print("Terminal velocity v = ", v_term)

    return v_term


def dragForce():
    print("Drag Force")

    Cd = input("Drag coefficient>")
    if Cd not in Cd_dict:
        try:
            Cd = float(Cd)
        except ValueError:
            Cd = numeric(Cd)
    elif Cd in Cd_dict:
        Cd = Cd_dict[Cd]

    A = input("Frontal surface area> ")
    try:
        A = float(A)
    except ValueError:
        A = numeric(A)

    p = input("Medium density> ")
    try:
        p = float(p)
    except ValueError:
        p = numeric(p)

    v = input("Velocity> ")
    try:
        v = float(v)
    except ValueError:
        v = numeric(v)

    F_d = 0.5*Cd*p*v*v*A
    print("Drag force Fd = ", F_d)

    return F_d


