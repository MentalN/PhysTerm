from Utilities.Checkers import numeric
from Utilities.PlanetData import mPlanet
from Utilities.Constants import G


def force():
    print("Gravitational Force")
    m1 = input("Mass of the first object m1> ")
    if mPlanet(m1) is False:
        numeric(m1)
    else:
        m1 = mPlanet(m1)
    m2 = input("Mass of the second object m2> ")
    if mPlanet(m2) is False:
        numeric(m2)
    else:
        m1 = mPlanet(m2)
    r = numeric(input("Distance between the two objects> "))
    F = (G*m1*m2)/(r*r)
    print("Force of gravity F=",F)
    return F


def potential():
    print("Gravitational Potential")
    m1 = input("Mass of the first object m1> ")
    if mPlanet(m1) is False:
        numeric(m1)
    else:
        m1 = mPlanet(m1)
    m2 = input("Mass of the second object m2> ")
    if mPlanet(m2) is False:
        numeric(m2)
    else:
        m1 = mPlanet(m2)
    r = numeric(input("Distance between the two objects> "))
    U = (G*m1*m2)/(r)
    print("gravitational potential energy  U =", U)
    return U