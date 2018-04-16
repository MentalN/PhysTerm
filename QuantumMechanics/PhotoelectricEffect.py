#   File: PhotoelectricEffect.py
#   Author: Nawaf Abdullah
#   Creation Date: 9/April/2018
#   Description: Photoelectric effect calculations
from Utilities.Checkers import numeric, EMspectrum, pause
from Utilities.Constants import R_d, c, h
from Utilities.Logger import logger


def transition():
    print("Photoelectric Effect")

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

    Z = input("Atomic Number of the element> ")
    try:
        Z = int(Z)
    except ValueError:
        Z = numeric(Z)

    i = 1/(n_i**2)
    f = 2/(n_f**2)
    wav = R_d*(i-f)*Z**2
    wav = 1/wav

    print("Transition Wavelength l= ", wav)

    print("EM spectrum:", EMspectrum(wav))

    f = c/wav
    print("Corresponding frequency f =", f)

    E = h*f
    print("Energy of the photon E =", E)

    log_str = "Transition Wavelength l= " + str(wav) + "\n" \
              "                               " + "EM spectrum:" + str(EMspectrum(wav)) + "\n" \
              "                               " + "Corresponding frequency f =" + str(f) + "\n" \
              "                               " + "Energy of the photon E =" + str(E)
    logger(log_str)

    pause()
    return wav
