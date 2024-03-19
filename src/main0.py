# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       aden                                                         #
# 	Created:      3/13/2024, 8:18:46 AM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
# from vex import *
import vex
import math

# from robot_config import *
# import auton
from opcontrol import *
from preauton import *
from auton import *
from tune_pid import *
from util import *

preauton()

do_testing = False
if do_testing:
    print("do nothing")
else:
    print("start of main program")
    field_controller = vex.Competition(opcontrol, opcontrol)
