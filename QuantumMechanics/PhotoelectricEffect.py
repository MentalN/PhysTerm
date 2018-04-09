#   File: PhotoelectricEffect.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/April/2018
#   Description: Photoelectric effect calculations
from Utilities.Checkers import numeric, EMspectrum
from Utilities.Constants import R_d, c, h
from periodic.table import element


def transition():
    print("[1] - Hydrogen atom")
    print("[2] - Hydrogen like element")
    select = input("Enter the number of your selection> ")
    try:
        select = int(select)
    except ValueError:
        print("Entry not valid! ")
        transition()
    if select != 1 or select != 2:
        print("Entry not valid! ")
        transition()

    n_i = input("Initial orbit number ni> ")
    try:
        n_i = int(n_i)
    except ValueError:
        n_i = numeric(n_i)

    n_f = input("final orbit number nf> ")
    try:
        n_f = int(n_f)
    except ValueError:
        n_f = numeric(n_f)

    if select == 1:
        hydrogen(n_i, n_f)
    elif select == 2:
        hydrogenLike(n_i, n_f)


def hydrogen(ni, nf):
    wav = R_d*((1/ni**2)-(1/nf**2))
    wav = wav**-1

    print("Transition Wavelength l= ", wav)

    if ni == 1 and nf >= 2:
        print("Lyman series")
    elif ni == 2 and nf >= 3:
        print("Balmer series")
    elif ni == 3 and nf >= 4:
        print("Paschen series")
    elif ni == 4 and nf >= 5:
        print("Brackett series")
    elif ni == 5 and nf >= 6:
        print("Pfund series")
    elif ni == 6 and nf >= 7:
        print("Humphreys series")

    print("EM spectrum: ", print(EMspectrum(wav)))

    f = c/wav
    print("Corresponding frequency f= ", f)

    E = h*f
    print("Energy of the photon E= ", E)

    return wav


def hydrogenLike(ni, nf):
    Z = element(input("name of element> "))
    try:
        Z = Z.atomic
    except AttributeError:
        print("Invalid entry!")

    wav = R_d*Z*Z*((1/ni**2)-(1/nf**2))
    wav = wav**-1

    print("Transition Wavelength l= ", wav)

    print("EM spectrum: ", print(EMspectrum(wav)))

    f = c/wav
    print("Corresponding frequency f= ", f)

    E = h*f
    print("Energy of the photon E= ", E)

    return wav



