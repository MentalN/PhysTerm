#   File: Logger.py
#   Author: Nawaf Abdullah
#   Creation Date: 15/April/2018
#   Description: Logs all the outputs given by PhysTerm
from datetime import datetime


def logger(output):
    log = open("log.txt", "a")
    output = str(output)
    log_str = "[" + str(datetime.now()) + "] > " + output + "\n"
    log.write(log_str)

