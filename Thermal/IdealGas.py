#   File: IdealGas.py
#   Author: Nawaf Abdullah
#   Creation Date: 8/April/2018
#   Description: Ideal gas calculations
from Utilities.Constants import R
from Utilities.Checkers import numeric, pause
from sympy.solvers import solve
from sympy import Symbol


def idealGas():
    P = 0
    V = 0
    T = 0
    n = 0
    var_list = [[P, "pressure"], [V, "volume"], [T, "temperature"], [n, "moles number"]]
    print("Select a variable to solve for> ")
    print("[1] - pressure (P)")
    print("[2] - volume (V) ")
    print("[3] - temperature (T)")
    print("[4] - number of moles (n)")
    select = input("Enter the number of your selection> ")
    try:
        select = int(select)
    except ValueError:
        select = numeric(select)

    del var_list[select-1]

    def var_filler():
        for i in range(len(var_list)):
            print("Enter a value for ", var_list[i][1])
            var_list[i][0] = input("> ")
            try:
                var_list[i][0] = float(var_list[i][0])
            except ValueError:
                var_list[i][0] = numeric(var_list[i][0])

    if select == 1:
        P = Symbol('P')
        var_filler()
        result = solve(var_list[2][0] * R * var_list[1][0] - P * var_list[0][0], P)
    elif select == 2:
        V = Symbol('V')
        var_filler()
        result = solve(var_list[2][0] * R * var_list[1][0] - var_list[0][0] * V, V)
    elif select == 3:
        T = Symbol('T')
        var_filler()
        result = solve(var_list[2][0] * R * T - var_list[0][0] * var_list[1][0], T)
    elif select == 4:
        n = Symbol('n')
        var_filler()
        result = solve(n * R * var_list[2][0] - var_list[0][0] * var_list[1][0], n)
    else:
        print("Please enter a valid selection")
        idealGas()

    print(result)
    pause()
    return result
