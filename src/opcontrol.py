import vex
from src.robot_config import *

# Constants
TNK = 0
TSA = 1
OSA = 2

def opcontrol():
    SENSITIVITY = 0.85

    # Reset drive velocity
    drive_l.stop(vex.BrakeType.COAST)
    drive_r.stop(vex.BrakeType.COAST)

    while(True):
        # Set a "shift" key
        shifted = master.buttonL2.pressing()

        # Base layer
        if not shifted:
            intake.spin(FORWARD, (master.buttonR1.pressing() - master.buttonR2.pressing()) * 100, vex.VelocityPercentUnits)
            # l1 under

        # Shifted layer
        # if shifted:
            # l1 left
            # l2 right

        # y hang


        opdrive(TSA, 1.0, SENSITIVITY)

def opdrive(control_scheme, speed_mod, turn_mod):
    axis_rx = master.axis1.value()
    axis_ry = master.axis2.value()
    axis_lx = master.axis3.value()
    axis_ly = master.axis4.value()
    # Tank drive
    if control_scheme == TNK:
        drive_r.spin(FORWARD, axis_ry * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, axis_lx * speed_mod, vex.VelocityUnits.PERCENT)
    elif control_scheme == TSA:
        drive_r.spin(FORWARD, (axis_lx - axis_rx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, (axis_lx + axis_rx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
    elif control_scheme == OSA:
        drive_r.spin(FORWARD, (axis_ly - axis_lx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, (axis_ly + axis_lx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
