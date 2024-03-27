import vex
from stddefs import *
from robot_config import *

# Top of file is new functions
# Bottom of file is making shorthand for long function names, like:
# src.robot_config.drive_r.position(vex.RotationUnits.REV)

# UTILITY FUNCTIONS

class EdgeDetection:
    def __init__(self, value):
        self.prev_val = value

    # Mostly used to toggle things on button press
    # Rising edge
    def is_redge(self, value):
        edge = False
        if self.prev_val < value:
            edge = True

        self.prev_val = value
        return edge

    # Mostly used to toggle things on button release
    # Falling edge
    def is_fedge(self, value):
        edge = False
        if self.prev_val > value:
            edge = True

        self.prev_val = value
        return edge

    # Not sure what the use case is, but I added it before I realized that
    def is_edge(self, value):
        edge = False
        if not self.prev_val == value:
            edge = True

        self.prev_val = value
        return edge

def stop_distance(velocity, acceleration, target_velocity = 0):
    return -(target_velocity ** 2 - velocity ** 2 ) / (2 * acceleration);

def handle_acceleration(position, distance, velocity, max_velocity, acceleration, tick_rate, do_decel):
    if (abs(position) + stop_distance(velocity, acceleration) >= abs(distance)) and do_decel:
        return velocity - acceleration / tick_rate
    if velocity < max_velocity:
        return velocity + acceleration * tick_rate
    return max_velocity

def within_range(value, base_value, range):
    return value <= base_value + range and value >= base_value - range

# SHORTHAND
global DRIVE_REV_TO_IN
DRIVE_REV_TO_IN = MEDIUM_OMNI_CIRC * (36.0/48.0)

def pos_drive_r():
    return drive_r.position(REV) * DRIVE_REV_TO_IN
def pos_drive_l():
    return drive_l.position(REV) * DRIVE_REV_TO_IN
def vel_drive_r():
    return drive_r.velocity(vex.RPM) * DRIVE_REV_TO_IN
def vel_drive_l():
    return drive_l.velocity(vex.RPM) * DRIVE_REV_TO_IN

def imu_rotation():
    return imu.rotation() * all_globals.imu_correction

# Controller joystick shorthand
def axis_rx():
    return master.axis1.value()
def axis_ry():
    return master.axis2.value()
def axis_lx():
    return master.axis3.value()
def axis_ly():
    return master.axis4.value()

# Control back button shorthand
def btn_r1():
    return master.buttonR1.pressing()
def btn_r2():
    return master.buttonR2.pressing()
def btn_l1():
    return master.buttonL1.pressing()
def btn_l2():
    return master.buttonL2.pressing()

# Controller front button shorthand
def btn_a():
    return master.buttonA.pressing()
def btn_b():
    return master.buttonB.pressing()
def btn_x():
    return master.buttonX.pressing()
def btn_y():
    return master.buttonY.pressing()

def btn_right():
    return master.buttonRight.pressing()
def btn_left():
    return master.buttonLeft.pressing()
def btn_up():
    return master.buttonUp.pressing()
def btn_down():
    return master.buttonDown.pressing()
