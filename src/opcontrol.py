import vex
from robot_config import *
from util import *

# Constants
TNK = 0
TSA = 1
OSA = 2

def opcontrol():
    SENSITIVITY = 0.85

    # Set up edge detection
    fold_switch = EdgeDetection(False)
    wing_r_switch = EdgeDetection(False)
    wing_l_switch = EdgeDetection(False)

    # Reset drive velocity
    drive_l.stop(COAST)
    drive_r.stop(COAST)

    while(True):
        # Drivetrain
        opdrive(TSA, 1.0, SENSITIVITY)

        # Elevation
        hang.spin(FORWARD, (btn_right() - btn_y()) * 100, PERCENT)

        # Set a "shift" key
        shifted = btn_l2()

        # Base layer
        if not shifted:
            # Intake
            intake.spin(FORWARD, (btn_r1() - btn_r2()) * 100, PERCENT)
            # Change intake height
            intake_fold.set(fold_switch.is_redge(btn_l1()))

        # Shifted layer
        if shifted:
            # Wings
            wing_l.set(wing_l_switch.is_redge(btn_l1()))
            wing_r.set(wing_r_switch.is_redge(btn_r1()))

        vex.wait(20, MSEC)

def opdrive(control_scheme, speed_mod, turn_mod):
    # Tank drive
    if control_scheme == TNK:
        drive_r.spin(FORWARD, axis_ry() * speed_mod, PERCENT)
        drive_l.spin(FORWARD, axis_lx() * speed_mod, PERCENT)
    # Two stick arcade
    elif control_scheme == TSA:
        drive_r.spin(FORWARD, (axis_lx() - axis_rx() * turn_mod) * speed_mod, PERCENT)
        drive_l.spin(FORWARD, (axis_lx() + axis_rx() * turn_mod) * speed_mod, PERCENT)
    # One stick arcade
    elif control_scheme == OSA:
        drive_r.spin(FORWARD, (axis_ly() - axis_lx() * turn_mod) * speed_mod, PERCENT)
        drive_l.spin(FORWARD, (axis_ly() + axis_lx() * turn_mod) * speed_mod, PERCENT)
