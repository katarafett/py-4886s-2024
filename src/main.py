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

from robot_config import *
import auton
import opcontrol
import preauton
import tune_pid
import util

preauton.preauton()

do_testing = True
if do_testing:
    print("do nothing")
else:
    field_controller = vex.Competition(opcontrol.opcontrol, auton.autonomous)
