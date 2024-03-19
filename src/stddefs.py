# Transferred from stddefs.h, so incomplete. I've not made shorthand for every
# unit or unit conversion

import math
import vex
# Conversions
global RAD_TO_DEG
RAD_TO_DEG = 57.29578

# Wheel sizes
global LARGE_OMNI_DIAM
LARGE_OMNI_DIAM = 4.0
global MEDIUM_OMNI_DIAM
MEDIUM_OMNI_DIAM = 3.25
global SMALL_OMNI_DIAM
SMALL_OMNI_DIAM = 2.75
global LARGE_WHEEL_DIAM
LARGE_WHEEL_DIAM = 5.0
global MEDIUM_WHEEL_DIAM
MEDIUM_WHEEL_DIAM = 4.0
global SMALL_WHEEL_DIAM
SMALL_WHEEL_DIAM = 2.75
global TRACT_WHEEL_DIAM
TRACT_WHEEL_DIAM = 3.25

global LARGE_OMNI_CIRC
LARGE_OMNI_CIRC = LARGE_OMNI_DIAM * math.pi
global MEDIUM_OMNI_CIRC
MEDIUM_OMNI_CIRC = MEDIUM_OMNI_DIAM * math.pi
global SMALL_OMNI_CIRC
SMALL_OMNI_CIRC = SMALL_OMNI_DIAM * math.pi
global LARGE_WHEEL_CIRC
LARGE_WHEEL_CIRC = LARGE_WHEEL_DIAM * math.pi
global MEDIUM_WHEEL_CIRC
MEDIUM_WHEEL_CIRC = MEDIUM_WHEEL_DIAM * math.pi
global SMALL_WHEEL_CIRC
SMALL_WHEEL_CIRC = SMALL_WHEEL_DIAM * math.pi
global TRACT_WHEEL_CIRC
TRACT_WHEEL_CIRC = TRACT_WHEEL_DIAM * math.pi

# Unit shorthand
global REV
REV = vex.RotationUnits.REV
global DEG
DEG = vex.RotationUnits.DEG

# Globally tracked things
class TrackedGlobals:
    def __init__(self, target_heading, wheel_to_wheel_dist, imu_correction):
        self.target_heading = target_heading
        self.wheel_to_wheel_dist = wheel_to_wheel_dist
        self.imu_correction = imu_correction
    def set_target_heading(self, value):
        self.target_heading = value
    def inc_target_heading(self, value):
        self.target_heading += value
