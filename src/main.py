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

from src.robot_config import *
from src import auton
from src import opcontrol
from src import preauton
from src import tune_pid
from src import util

preauton.preauton()

do_testing = False
if do_testing:
    field_controller = vex.Competition(opcontrol.opcontrol, auton.autonomous)
else:
    print("do nothing")
