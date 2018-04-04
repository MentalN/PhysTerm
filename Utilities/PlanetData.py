#   File: main.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: support module for PhysTerm. Solar system planets data.
#   Reference: NASA Solar System Exploration webpage


masses = {'jupiter': 1.90e27, 'saturn': 5.68e26, 'neptune': 1.02e26, 'uranus': 8.68e25,
          'earth':   5.97e24, 'venus':  4.87e24, 'mars':    6.40e23, 'mercury':3.30e23,
          'ganymede':1.48e23, 'titan':  1.30e23, 'callisto':1.08e23, 'io':     8.93e22,
          'europa':  4.80e22, 'triton': 2.10e22, 'eris':    1.67e22, 'pluto':  1.31e22,
          'titania': 3.40e21, 'oberon': 2.90e21, 'rhea':    2.30e21, 'lapetus':1.80e21,
          'charon':  1.55e21, 'ariel':  1.30e21, 'umbriel': 1.20e21, 'dione':  1.10e21,
          'ceres':   9.35e20, 'tethys': 6.18e20, 'vesta':   2.71e20, 'pallas': 2.41e20,
          'enceladus':1.1e20, 'miranda':6.60e19, 'proteus': 5.00e19, 'mimas':  3.75e19}


def mPlanet(name):
    name = name.lower()
    if name in masses:
        return masses[name]

