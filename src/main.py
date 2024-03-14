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
from vex import *

import robot_config
import auton
import opcontrol
import preauton
import tune_pid
import util

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")
