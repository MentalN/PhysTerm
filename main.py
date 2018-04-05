#   File: main.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: main menu of PhysTerm. Program runtime starts here.
from cursesmenu import *
from cursesmenu.items import *

#   '_i'  = item in main_menu
#   '_sm' = submenu



#TODO: cursesMenu is a no-go, find another way to implment menu
"""
def main():
#   Main menu declaration
    main_menu = CursesMenu("PhysTerm", "Select a field:")
#   Mechanics: Submenu declaration
    mech_sm = CursesMenu("Mechanics", "Select an operation:")
#   Mechanics: add function items for submenu
#    mech_f1 = FunctionItem("Gravitational Force", Gravity.gForce())
    mech_f2 = FunctionItem("Gravitational Potential", Gravity.gPotential())
#   Mechanics: append items to Submenu
    mech_sm.append_item(mech_f1)
    mech_sm.append_item(mech_f2)
    mech_i = SubmenuItem("Mechanics", submenu=mech_sm)
    main_menu.append_item(mech_i)
    main_menu.start()
    main_menu.join()
"""



