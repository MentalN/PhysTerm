#   File: main.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: main menu of PhysTerm. Program runtime starts here.
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


def main():
    print("You can type 'list' for available options")
    entry = input("PhysTerm>> ")
    if entry.lower() == "mechanics":
        mech()
    elif entry.lower() == "em":
        em()
    elif entry.lower() == "thermal":
        thermal()
    elif entry.lower() == "quantum":
        quantum()
    elif entry.lower() == "list":
        help_main()
    elif entry.lower() == 'exit':
        exit()
    else:
        print("Command not found!")
        main()
    main()


def mech():
    def mech_help():
        print("Entries: ")
        print("gravity")
        print("drag")
        mech()

    drag_dict = {"terminal velocity": terminalVelocity, "force": dragForce}
    gravity_dict = {"force": gForce, "potential": gPotential}

    entry = input("PhysTerm>Mechanics>> ")

    if entry.lower() == "drag":
        entry2 = input("PhysTerm>Mechanics>Drag>> ")

        if entry2.lower() in drag_dict:
            drag_dict[entry2]()
        else:
            print("Command not found!")
            mech()

    elif entry.lower() == "gravity":
        entry2 = input("PhysTerm>Mechanics>Gravity>> ")

        if entry2.lower() in gravity_dict:
            gravity_dict[entry2]()
        else:
            print("Command not found!")
            mech()

    elif entry.lower() == "list":
        mech_help()


def em():
    def em_help():
        print("Entries: ")
        print("equivalent")

    eqv_dict = {"equivalent": eqv_selector}

    entry = input("PhysTerm>E&M>> ")

    if entry.lower() == "equivalent":
        print("Select element: 'resistors', 'capacitors', or 'inductors'")
        entry2 = input("PhysTerm>E&M>CircuitEquivalent>> ")

        if entry2.lower() == "resistors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>resistors>> ")
            if entry3 == "parallel":
                eqv_dict["equivalent"](1)
            elif entry3 == "series":
                eqv_dict["equivalent"](2)

        elif entry2.lower() == "capacitors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>capacitors>> ")
            if entry3 == "parallel":
                eqv_dict["equivalent"](3)
            elif entry3 == "series":
                eqv_dict["equivalent"](4)

        elif entry2.lower() == "inductors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>inductors>> ")
            if entry3 == "parallel":
                eqv_dict["equivalent"](5)
            elif entry3 == "series":
                eqv_dict["equivalent"](6)

        else:
            print("Command not found!")
            em()

    elif entry.lower() in eqv_dict:
            eqv_dict[entry.lower()]()

    elif entry.lower() == "list":
        em_help()

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        em()


def thermal():
    def thermal_help():
        print("Entries: ")
        print("ideal gas")
        thermal()

    therm_dict = {"ideal gas": idealGas}
    entry = input("PhysTerm>Thermal>> ")
    if entry.lower() in therm_dict:
        therm_dict[entry.lower()]()

    elif entry.lower() == "list":
        thermal_help()

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        thermal()


def quantum():
    def qm_help():
        print("Entries: ")
        print("transition")
        quantum()

    qm_dict = {"transition": transition}
    entry = input("PhysTerm>Quantum>> ")
    if entry.lower() in qm_dict:
        qm_dict[entry.lower()]()

    elif entry.lower() == "list":
        qm_help()

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        quantum()


def help_main():
    print("Entries: ")
    print("'mechanics' for classical mechanics")
    print("'em' for electricity and magnetism")
    print("'Thermal' for Thermal Physics")
    print("'quantum' for Quantum Mechanics")
    print("'exit' terminates the program")
    main()


main()
