#   File: Gravity.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: Gravity calculations

from Utilities.Checkers import numeric
from Utilities.PlanetData import mPlanet
from Utilities.Constants import G


def gForce():
    print("Gravitational Force")

    m1 = input("Mass of the first object m1> ")
    if mPlanet(m1) is False:
        try:
            m1 = float(m1)
        except ValueError:
            m1 = numeric(m1)
    else:
        m1 = mPlanet(m1)

    m2 = input("Mass of the second object m2> ")
    if mPlanet(m2) is False:
        try:
            m2 = float(m2)
        except ValueError:
            m2 = numeric(m2)
    else:
        m2 = mPlanet(m2)

    r = input("Distance between two objects> ")
    try:
        r = float(r)
    except ValueError:
        r = numeric(r)

    F = G*m1*m2/(r*r)
    print("Force of gravity F=", F)

    return F


def gPotential():
    print("Gravitational Potential")

    m1 = input("Mass of the first object m1> ")
    if mPlanet(m1) is False:
        try:
            m1 = float(m1)
        except ValueError:
            m1 = numeric(m1)
    else:
        m1 = mPlanet(m1)

    m2 = input("Mass of the second object m2> ")
    if mPlanet(m2) is False:
        try:
            m2 = float(m2)
        except ValueError:
            m2 = numeric(m2)
    else:
        m2 = mPlanet(m2)

    r = input("Distance between two objects> ")
    try:
        r = float(r)
    except ValueError:
        r = numeric(r)

    U = G*m1*m2/(r)
    print("gravitational potential energy  U =", U)

    return U


