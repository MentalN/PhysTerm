#   File: main.py
#   Author: Nawaf Abdullah
#   Creation Date: 4/April/2018
#   Description: main menu of PhysTerm. Program runtime starts here.
# Mechanics Imports
from Mechanics.Gravity import *
from Mechanics.Drag import *
# ElectricityMagnetism Imports
from ElectricityMagnetism.CircuitEquivalents import *
# Thermal Imports
from Thermal.IdealGas import *
# Quantum Mechanics Imports
from QuantumMechanics.PhotoelectricEffect import *


#   TODO: Log calculations in a .txt or .xml format
#   TODO: Add the ability to adjust settings

#   Main interface
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


#   Main interface redirects to Mech for mechanics problems
def mech():
    #   Dictionaries holding the imported physics functions
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
        print("Available commands for Drag: ")
        for key in drag_dict:
            print("> ", key)
        print("Available commands for Gravity: ")
        for key in gravity_dict:
            print("> ", key)


#   Main interface redirects to em for E&M problems
def em():
    #   Dictionaries holding the imported physics functions
    em_dict = {"equivalent": eqv_selector}

    entry = input("PhysTerm>E&M>> ")

    if entry.lower() == "equivalent":
        print("Select element: 'resistors', 'capacitors', or 'inductors'")
        entry2 = input("PhysTerm>E&M>CircuitEquivalent>> ")

        if entry2.lower() == "resistors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>resistors>> ")
            if entry3 == "parallel":
                em_dict["equivalent"](1)
            elif entry3 == "series":
                em_dict["equivalent"](2)

        elif entry2.lower() == "capacitors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>capacitors>> ")
            if entry3 == "parallel":
                em_dict["equivalent"](3)
            elif entry3 == "series":
                em_dict["equivalent"](4)

        elif entry2.lower() == "inductors":
            print("select: 'parallel' or 'series'")
            entry3 = input("PhysTerm>E&M>CircuitEquivalent>inductors>> ")
            if entry3 == "parallel":
                em_dict["equivalent"](5)
            elif entry3 == "series":
                em_dict["equivalent"](6)

        else:
            print("Command not found!")
            em()

    elif entry.lower() in em_dict:
            em_dict[entry.lower()]()

    elif entry.lower() == "list":
        print("Available commands: ")
        for key in em_dict:
            print("> ", key)

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        em()


#   Main interface redirects to thermal for thermal physics problems
def thermal():
    #   Dictionaries holding the imported physics functions
    therm_dict = {"ideal gas": idealGas}
    entry = input("PhysTerm>Thermal>> ")
    if entry.lower() in therm_dict:
        therm_dict[entry.lower()]()

    elif entry.lower() == "list":
        print("Available commands: ")
        for key in therm_dict:
            print("> ", key)

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        thermal()


#   Main interface redirects to quantum for quantum mechanics problems
def quantum():
    #   Dictionaries holding the imported physics functions
    qm_dict = {"transition": transition}
    entry = input("PhysTerm>Quantum>> ")
    if entry.lower() in qm_dict:
        qm_dict[entry.lower()]()

    elif entry.lower() == "list":
        print("Available commands: ")
        for key in qm_dict:
            print("> ", key)

    elif entry.lower() == "exit":
        exit()

    else:
        print("Command not found!")
        quantum()


#   main interface redierects to help_main to show the user available commands
def help_main():
    print("Commands: ")
    print("'mechanics' for classical mechanics")
    print("'em' for electricity and magnetism")
    print("'Thermal' for Thermal Physics")
    print("'quantum' for Quantum Mechanics")
    print("'exit' terminates the program")
    main()


main()
