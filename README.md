# PhysTerm

PhysTerm is a terminal program written in Python 3.6 that performs a variaty of calculations of in different fields of physics.


# Running The Program
PhysTerm is ran from terminal using python. In Windows command prompt, this done using the following command:
      
      > python PhysTerm.py

and in Linux:

      > python3 PhysTerm.py

Running the program with full functionality requires the following dependecies:
 -SymPy

During runtime, the program itself have built-in commands to guide the user through the program:
 - The user can type "list" anytime during the program runtime to display the available commands the user can type in to perform a specific calculation or to select a field.
 - the user can type "exit" to terminate the program.

When the user inputting values for some physics calculations, they can just type in the "name" of a value, for instance:
 - When calculating gravitational force, the user can type "venus" when inputting mass to get the mass of planet Venus.
 - When calculating drag force, the user can type "sphere" when inputting drag coeffecient to get to get the value for sphere

PhysTerm also logs all functions outputs during program runtime to a file log.txt
 

# Current Available Functions
Mechanics:  - Drag [Terminial Velocity - Drag Force]
            - Gravity [g Force, g Potential]

E & M:      - Circuit Equivalents [Resistors - Capacitors - Inductors]

Thermal:    - Ideal Gas Equation

Quantum Mechanics:      - Photoelectric effect


# Growing PhysTerm
PhysTerm code was designed in a way to allow adding more physics functions easily by just adding the code to the appropriate directory, and then updating the relevant dictionary in main. The long-term goal of this project is to have the program able to solve all problems from all areas in physics.
