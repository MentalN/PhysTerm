#   File: main.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: main menu of PhysTerm. Program runtime starts here.
from cursesmenu import CursesMenu
from cursesmenu.items import *
# Mechanics Imports
from Mechanics.Drag import *
from Mechanics.Gravity import *
from Mechanics.Drag import *
# ElectricityMagnetism Imports
from ElectricityMagnetism.CircuitEquivalents import *
# Thermal Imports
from Thermal.IdealGas import *
# Quantum Mechanics Imports
from QuantumMechanics.PhotoelectricEffect import *

#   '_i'  = item in main_menu
#   '_sm' = submenu


#   Main menu declaration
main_menu = CursesMenu("PhysTerm", "Select a field:")

#   Mechanics: Submenu declaration
mech_sm = CursesMenu("Mechanics", "Select an operation:")
#   Mechanics: add function items for submenu
mech_f1 = FunctionItem("Gravity: gravitational Force", gForce)
mech_f2 = FunctionItem("Gravity: gravitational Potential", gPotential)
mech_f3 = FunctionItem("Drag: terminal velocity", terminalVelocity)
mech_f4 = FunctionItem("Drag: drag force", dragForce)
#   Mechanics: append items to Submenu
mech_sm.append_item(mech_f1)
mech_sm.append_item(mech_f2)
mech_sm.append_item(mech_f3)
mech_sm.append_item(mech_f4)
mech_i = SubmenuItem("Mechanics", submenu=mech_sm)


#   EM: Submenu declaration
em_sm = CursesMenu("ElectricityMagnetism", "Select an operation:")
#   EM: add function items for submenu
em_f1 = FunctionItem("Circuit Equivalent: parallel Resistors", parallelResistors)
em_f2 = FunctionItem("Circuit Equivalent: series Resistors", seriesResistors)
em_f3 = FunctionItem("Circuit Equivalent: parallel Capacitors", parallelCapacitors)
em_f4 = FunctionItem("Circuit Equivalent: series Capacitors", seriesCapacitors)
em_f5 = FunctionItem("Circuit Equivalent: parallel Inductors", parallelInductors)
em_f6 = FunctionItem("Circuit Equivalent: series Inductors", seriesInductors)
#   EM: append items to Submenu
em_sm.append_item(em_f1)
em_sm.append_item(em_f2)
em_sm.append_item(em_f3)
em_sm.append_item(em_f4)
em_sm.append_item(em_f5)
em_sm.append_item(em_f6)
em_i = SubmenuItem("ElectricityMagnetism", submenu=em_sm)


#   Thermo: Submenu declaration
thermo_sm = CursesMenu("Thermal Physics", "Select an operation:")
#   Thermo: add function items for submenu
thermo_f1 = FunctionItem("Ideal Gas Law", idealGas)
#   Thermo: append items to Submenu
thermo_sm.append_item(thermo_f1)
thermo_i = SubmenuItem("Thermal Physics", submenu=thermo_sm)


#   QM: Submenu declaration
qm_sm = CursesMenu("Quantum Mechanics", "Select an operation:")
#   QM: add function items for submenu
qm_f1 = FunctionItem("Photoelectric effect", transition)
#   QM: append items to Submenu
qm_sm.append_item(qm_f1)
qm_i = SubmenuItem("Quantum Mechanics", submenu=qm_sm)


main_menu.append_item(mech_i)
main_menu.append_item(em_i)
main_menu.append_item(thermo_i)
main_menu.append_item(qm_i)
main_menu.start()
main_menu.join()
