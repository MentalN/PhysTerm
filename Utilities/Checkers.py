#   File: Checkers.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: several functions that checks for input


#   Checks if entry is a number and make sure it is in case if it's not
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


#   Returns the wavelength position on the Electromagnetic Spectrum
def EMspectrum(L):
    L = abs(L)
    if L <= 1e-11:
        em_spec = "Gamma Rays"
    elif 1e-8 >= L >= 1e-11:
        em_spec = "X-Rays"
    elif 390e-09 >= L >= 1e-8:
        em_spec = "Ultraviolet"
    elif 700e-09 <= L <= 390e-09:
        em_spec = "Visible light"
    elif 1e-3 <= L <= 700e-09:
        em_spec = "Infrared"
    elif 1e-1 <= L <= 1e-3:
        em_spec = "Microwaves"
    elif L >= 1e-3:
        em_spec = "Radio waves"
    return em_spec


#   Pauses the program so that the user can see the output
def pause():
    cmd = input("Type anything to continue, or 'exit' to terminate> ")
    if cmd == "exit":
        exit()
    else:
        pass
